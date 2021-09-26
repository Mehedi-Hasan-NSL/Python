from data_load import *
#from model import autoencoder
from keras.models import load_model
import cv2

root_dir = os.path.dirname(os.path.abspath(__file__))
model_name = "autoendcoder_best.h5"
model_path = os.path.join(root_dir, "models")
model = os.path.join(model_path, model_name)
autoencoder = load_model(model)


## predictions for all the test data
#predictions = autoencoder.predict(test_data)

#display(test_data, predictions)


## input one single image 

input_image_idx = 10
test_image = test_data[input_image_idx]
plt.imshow(test_image.reshape(28,28))
plt.gray()
plt.show()
test_image = np.expand_dims(test_image, axis=0)
#print(test_image.shape)
prediction = autoencoder.predict(test_image)
#print(prediction.shape)

cv2.imwrite(root_dir + "/test.jpg", prediction.reshape(28,28))
plt.imshow(prediction.reshape(28,28))
plt.gray()
plt.show()

