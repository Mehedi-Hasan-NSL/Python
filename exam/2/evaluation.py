from utils import *
from data_load import *
import warnings
warnings.filterwarnings("ignore") 

root_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(root_dir, "models")

model_name = "autoendcoder_best.h5"
model = os.path.join(model_path, model_name)
autoencoder = load_model(model)

print("EValuation on train ")

autoencoder.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])

history_train = autoencoder.evaluate(x=train_data,
								y=train_target,
								batch_size=128,
								verbose =1,
							)

print("EValuation on test")
history_test = autoencoder.evaluate(x=test_data,
								y=test_target,
								batch_size=128,
								verbose =1
							)

print("EValuation on validation")
history_val = autoencoder.evaluate(x=val_data,
								y=val_target,
								batch_size=128,
								verbose =1,
							)

#print("Avg of loss", ((history2+history3+history4) / 3))

loss = np.average([history_train[0], history_test[0], history_val[0]])
acc = np.average([history_train[1], history_test[1], history_val[1]])

## ploting th
plt.scatter(loss, acc, alpha=1)
plt.xlabel("Avg Loss")
plt.ylabel("Avg Accuracy")
plt.show()