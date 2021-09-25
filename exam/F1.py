import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

x_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_train = np.array([5*i**2 + 7*i + 9 for i in x_train])


## build a model 
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, input_shape=(1,), activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
	tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(loss= tf.keras.losses.Huber(),
    optimizer = Adam())

model.fit(x_train, y_train, epochs=5000, batch_size=100)

prediction = model.predict(x_train)
for i in x_train:
	print('input : ', i, 'Output: ', *[int(np.round(prediction[i]))])
