
****exam.yaml -> Environment
****train_log.txt -> training log file 
****logs -> directory contains tensorboard logs


1.Environment file : exam.yml

2.data_load.py contains MNIST data 

3. synthetic_data_generation.py genrate synthetic font image data and save i to synth_data folder 

4.data_load.py contains MNIST data train, test, val split 
	and process.py file to process the data for training 

5.model.py contains model architecture that  predict font digit image from handwritten input digit image

6.model_train.py contains the model training process and shows the prediction on test data 

7.evaluation.py contains that test the model on test, validation and train set and calculate average performance metrics and plot it in
	the notebook
8.inference.py predict on a single test handwritten image and ouputs a font image data 

9.visualize_layer.py visualize the last 2nd layer 
