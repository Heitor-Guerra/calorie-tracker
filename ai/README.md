# Food-101 Image Classification with MobileNetV2

This project trains an image classification model on the Food-101 dataset using TensorFlow.

The model uses an ImageNet-pretrained MobileNetV2 feature extractor with a custom classification layer for recognizing food.

---------------

# Requirements

    Python 3.12

Install the dependencies with:

```bash
pip install tensorflow tensorflow-datasets matplotlib
```

---------------

## Dataset

The script automatically downloads and loads the Food-101 dataset through TensorFlow Datasets.

Food-101 contains:

    101 food categories
    750 training images per category
    250 validation images per category
    101,000 images in total


---------------

## Model Architecture

The model consists of two main parts:

- ### Feature extractor
  A pretrained MobileNetV2 model is loaded with ImageNet weights. Its weights are frozen to avoid fine-tuning it.

- ### Classification head
  The custom head contains:
    Global average pooling,
    Dropout,
    A dense layer,
    Softmax activation,

-----------------

## Data Preprocessing

All images are resized to: 256 × 256 pixels

Pixel values are rescaled from the range [0, 255] to approximately [-1, 1], matching the preprocessing expected by MobileNetV2.
python

The training data optionally uses the following augmentations:

- Random horizontal flipping
- Random rotation between -20% and 20%

Validation images are resized and rescaled but are not augmented.

------------------

## Saving the Model

To save the trained model after training, add:

```python
model.save("food_classifier_model.keras")
```

The model can later be loaded with:

```python
model = tf.keras.models.load_model("food_classifier_model.keras")
```

-----------

# Next Steps

The next steps to build a functional calorie tracker are:
- Build a food segmentation model (FoodSeg103 Dataset is apropriate)
- Build a weight estimation model (Don't know a usable dataset...)
- Connect the pieces and test on an own dataset
