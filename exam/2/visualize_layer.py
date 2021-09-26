from utils import *
from data_load import *

#load model weights
root_dir = os.path.dirname(os.path.abspath(__file__))
model_name = "autoendcoder_best.h5"
model_path = os.path.join(root_dir, "models")
model = os.path.join(model_path , model_name)
autoencoder = load_model(model)


## input one single image 
input_image_idx = 10
test_image = test_data[input_image_idx]
plt.imshow(test_image.reshape(28,28))
plt.gray()
plt.show()


#print(autoencoder.summary())
print("######## all layers #########")
model_layers = [ layer.name for layer in autoencoder.layers]
print('layer name : ',model_layers)

##taking the last 2nd layer activation 

conv2d_transpose_1_output = Model(inputs= autoencoder.input, outputs=autoencoder.get_layer('conv2d_transpose_1').output)
conv2d_transpose_1_pred = conv2d_transpose_1_output.predict(test_image)

#print(conv2d_transpose_1_pred.shape)

#ploting the output images 
fig = plt.figure(figsize=(16,8))
columns = 8
rows = 4
for i in range(columns*rows):
    fig.add_subplot(rows, columns, i+1)
    plt.axis('off')
    plt.title('filter: ' + str(i))
    plt.imshow(conv2d_transpose_1_pred[:, :, 0, i])
    plt.gray()
plt.show()