from utils import *
from data_load import *
from config import *
from model import autoencoder

root_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(root_dir, "models")
##Tensorboard callback

callbacks = [
    tf.keras.callbacks.TensorBoard(
    log_dir= root_dir + "/logs",
    update_freq="epoch",
    )  
]

## model train
history =autoencoder.fit(
		x=train_data,
		y=train_target,
		epochs=200,
		batch_size=config.BATCH_SIZE,
		shuffle=True,
		validation_data=(val_data, val_target),
		callbacks = callbacks
	)

## save the trained model
autoencoder.save(model_path+'/autoendcoder_200_epochs.h5')


## predictions on test data 
predictions = autoencoder.predict(test_data)

## shwoing predictions output for 10 test images 
display(test_data, predictions)