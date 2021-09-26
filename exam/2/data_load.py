from utils import *
from preprocess import *

def target_process(data):
	data_list = []
	for i in data:
		img = cv2.imread(synth_data_path+'/digit_'+str(i)+'.jpg', 0)
		img = cv2.resize(img, (28, 28))
		img = np.reshape(img, (28, 28, 1))
		data_list.append(img)
	target = np.array(data_list)
	return target 


root_dir = os.path.dirname(os.path.abspath(__file__))
synth_data_path = os.path.join(root_dir, "synth_data")

## dataset load from keras 
(train_data, train_y), (test_data, test_y) = mnist.load_data()


## loading synthetic data as target data

train_target = target_process(train_y)
test_target = target_process(test_y)


### train, test, val split 

train_data = preprocess(train_data)
train_target = preprocess(train_target)

val_split = .2

val_data = train_data[ : int(val_split*len(train_data))]
val_target = train_target[ : int(val_split*len(train_y))]

test_data = preprocess(test_data)
test_target = preprocess(test_target)

#display(val_target, val_data)