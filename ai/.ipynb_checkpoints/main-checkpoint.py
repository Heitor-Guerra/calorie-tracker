# %% Imports

import matplotlib.pyplot as plt
import numpy as np
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
shuffle_buffer_size = 200
batch_size = 256
learning_rate = 1e-4
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
n_epochs = 50


# %% Training Parameters

# Classification: Cross Entropy Loss
criterion = tf.keras.losses.CategoricalCrossentropy()
img_size = 512
img_shape = (img_size, img_size, 3)
metrics = [
    tf.keras.metrics.Precision(),
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


ds_train = ds_train.map(
    lambda x, y: (resize_rescale(x), y), num_parallel_calls=tf.data.AUTOTUNE
)
ds_train = ds_train.cache()
ds_train = ds_train.shuffle(shuffle_buffer_size, reshuffle_each_iteration=True)
ds_train = ds_train.batch(batch_size)
ds_train = ds_train.prefetch(tf.data.AUTOTUNE)

if augmentation:
    ds_train = ds_train.map(
        lambda x, y: (train_transformation(x, training=True), y),
        num_parallel_calls=tf.data.AUTOTUNE,
    )

fig = tfds.show_examples(ds_train, ds_info, is_batched=True)


# %% Test dataset preparation
ds_test = ds_test.map(
    lambda x, y: (resize_rescale(x), y), num_parallel_calls=tf.data.AUTOTUNE
)
ds_test = ds_test.batch(batch_size)
ds_test = ds_test.cache()
ds_test = ds_test.prefetch(tf.data.AUTOTUNE)

fig = tfds.show_examples(ds_test, ds_info, is_batched=True)
