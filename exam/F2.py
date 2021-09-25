import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Conv2D, ReLU
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


### model parameters 
kernel_size = 3
filter_size = 32

###random data generate
height = 128
width = 128
c = 3
input_1 = np.random.rand(50,height, width, c)
input_2 = np.random.rand(50,height, width, c)


##input1
input1 = tf.keras.layers.Input(shape=(128, 128, 3),name= "input_1" )
conv_x = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), name= "conv_x" )(input1)
rel_x = tf.keras.layers.ReLU()(conv_x)

#input2
input2 = tf.keras.layers.Input(shape=(128, 128, 3), name = 'input_2')
conv_y = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), name = 'conv_y')(input2)
rel_y = tf.keras.layers.ReLU(name= "relu_x")(conv_y)

# equivalent to `added = tf.keras.layers.add([x1, x2])`
added = tf.keras.layers.Add(name= "relu_y")([rel_x, rel_y])

conv_z = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), name = 'conv_z')(added)
rel_z = tf.keras.layers.ReLU(name= "relu_z")(conv_z)


out = rel_z
model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

## test data generate 
## for random data generate test data should match 
## the model output shape 
x = height - kernel_size - 1
y = width - kernel_size - 1 
c = filter_size 
y_test = np.random.randint(0, 10, size=(50,x,y,c))

# fit the model with random generated inputs
history = model.fit(
      [input_1,input_2],
	  y_test,
      epochs=15,
	  batch_size=32,
      verbose=1)
