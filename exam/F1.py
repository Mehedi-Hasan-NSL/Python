import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
#from sklearn.preprocessing import PolynomialFeatures

def poly_input(i):
    return [1, i, i*i]

x_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_train = np.array([5*i**2 + 7*i + 9 for i in x_train])

x_train = np.array([poly_input(i) for i in x_train])

#print(x_train_expanded.shape)
#print(y_train.shape)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, input_shape=(3,), activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
	tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(loss= tf.keras.losses.Huber(),
    optimizer = Adam())

model.fit(x_train, y_train, epochs=5000, batch_size=100)


for i in x_train:
	print('input : ', i, ',Output: ', round(model.predict([poly_input(i)])[0][0]))