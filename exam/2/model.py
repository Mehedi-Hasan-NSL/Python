from utils import *
from config import *

input = layers.Input(shape=(28, 28, 1))

# Encoder
x = layers.Conv2D(config.FILTER_SIZE, config.KERNEL_SIZE, activation="relu", padding="same")(input)
x = layers.MaxPooling2D((2, 2), padding="same")(x)
x = layers.Conv2D(config.FILTER_SIZE, config.KERNEL_SIZE, activation="relu", padding="same")(x)
x = layers.MaxPooling2D((2, 2), padding="same")(x)

# Decoder
x = layers.Conv2DTranspose(config.FILTER_SIZE, config.KERNEL_SIZE, strides=2, activation="relu", padding="same")(x)
x = layers.Conv2DTranspose(config.FILTER_SIZE, config.KERNEL_SIZE, strides=2, activation="relu", padding="same")(x)
x = layers.Conv2D(1, config.KERNEL_SIZE, activation="relu", padding="same")(x)

#x = layers.Flatten()(x)
#x = layers.Dense(28*28, activation="sigmoid")(x)
# Autoencoder
autoencoder = Model(input, x)
autoencoder.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])
print(autoencoder.summary())