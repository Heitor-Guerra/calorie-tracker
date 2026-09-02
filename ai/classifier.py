# %% Imports

import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds

# %% Dataset

(ds_train, ds_test), ds_info = tfds.load(
    "food101",
    with_info=True,
    shuffle_files=True,
    split=["train", "validation"],
    as_supervised=True,
)

print(ds_train)


# %% Hyperparameters

num_classes = ds_info.features["label"].num_classes
augmentation = True
shuffle_buffer_size = 100
batch_size = 64
learning_rate = 1e-4
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
n_epochs = 20


# %% Training Parameters

# Classification: Cross Entropy Loss
criterion = tf.keras.losses.SparseCategoricalCrossentropy()
img_size = 256
img_shape = (img_size, img_size, 3)
metrics = [
    tf.keras.metrics.SparseTopKCategoricalAccuracy(),
]

# %% Data Augmentation

resize_rescale = tf.keras.Sequential(
    [
        tf.keras.layers.Resizing(img_size, img_size),
        tf.keras.layers.Rescaling(1.0 / 127.5, offset=-1),
    ]
)

train_transformation = tf.keras.Sequential(
    [
        tf.keras.layers.RandomFlip(mode="horizontal"),
        tf.keras.layers.RandomRotation(factor=(-0.2, 0.2)),
    ]
)


# %% Train dataset preparation

fig = tfds.show_examples(ds_train, ds_info)

train = ds_train.map(
    lambda x, y: (resize_rescale(x), y), num_parallel_calls=tf.data.AUTOTUNE
)
train = train.shuffle(shuffle_buffer_size, reshuffle_each_iteration=True)
train = train.batch(batch_size)
if augmentation:
    train = train.map(
        lambda x, y: (train_transformation(x, training=True), y),
        num_parallel_calls=tf.data.AUTOTUNE,
    )
train = train.prefetch(tf.data.AUTOTUNE)


# %% Test dataset preparation

fig = tfds.show_examples(ds_test, ds_info)

test = ds_test.map(
    lambda x, y: (resize_rescale(x), y), num_parallel_calls=tf.data.AUTOTUNE
)
test = test.batch(batch_size)
test = test.cache()
test = test.prefetch(tf.data.AUTOTUNE)


# %% Feature Extraction Model definition

feature_extraction_model = tf.keras.applications.MobileNetV2(
    input_shape=img_shape, include_top=False, weights="imagenet"
)

feature_extraction_model.trainable = False

feature_extraction_model.summary()


# %% Classification model definition

# Some layers need to be instatiated before being used
global_pooling = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer = tf.keras.layers.Dense(num_classes, activation="softmax")


inputs = tf.keras.Input(shape=img_shape)
output = feature_extraction_model(inputs, training=False)
output = global_pooling(output)
output = tf.keras.layers.Dropout(0.2)(output)
output = prediction_layer(output)

model = tf.keras.Model(inputs, output)

model.summary()


# %% Model Compile

model.compile(optimizer=optimizer, loss=criterion, metrics=metrics)


# %% Model Training

history = model.fit(
    train,
    batch_size=batch_size,
    epochs=n_epochs,
    validation_data=test,
    validation_batch_size=batch_size,
)

acc = history.history["accuracy"]
loss = history.history["loss"]

plt.figure(figsize=(8, 8))

plt.subplot(2, 1, 1)
plt.plot(acc, label="Accuracy")
plt.legend(loc="lower right")
plt.ylabel("Accuracy")
plt.title("Accuracy")

plt.subplot(2, 1, 2)
plt.plot(loss, label="Loss")
plt.legend(loc="lower right")
plt.ylabel("Loss")
plt.title("Loss")
plt.xlabel("epoch")

plt.show()
