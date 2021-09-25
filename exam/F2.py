import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Conv2D, ReLU
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

height = 128
width = 128
c = 3

###random data generate

input_1 = np.random.rand(50,height, width, c)
input_2 = np.random.rand(50,height, width, c)


#print(input1)
#print(input2)

input1 = tf.keras.layers.Input(shape=(128, 128, 3))
conv_x = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu')(input1)
rel_x = tf.keras.layers.ReLU()(conv_x)

input2 = tf.keras.layers.Input(shape=(128, 128, 3))
conv_y = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu')(input2)
rel_y = tf.keras.layers.ReLU()(conv_y)

# equivalent to `added = tf.keras.layers.add([x1, x2])`
added = tf.keras.layers.Add()([rel_x, rel_y])

conv_z = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu')(added)
rel_z = tf.keras.layers.ReLU()(conv_z)
#out = tf.keras.layers.Dense(4)(rel_z)

out = rel_z
model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

y_test = np.random.randint(0, 10, size=(50, 1))
history = model.fit(
      [input_1,input_2],
	  y_test,
      epochs=15,
	  batch_size=32,
      verbose=1)