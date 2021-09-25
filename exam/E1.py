import numpy as np
import PIL
from PIL import Image
from PIL import ImageOps
import os 

root_dir = os.path.dirname(os.path.abspath(__file__))
r_img = os.makdirs(os.path.join(root_dir,"img"), exist_ok=True)

image_file = PIL.Image.open(root_dir+"/E1.png")
image_file = ImageOps.grayscale(image_file) 
image_array = np.array(image_file)

image_array = 255 - image_array

for i in range(image_array.shape[0]):
    for j in range(image_array.shape[1]):
        if (image_array[i,j]) < 50 :
            image_array[i,j] = 0
        else:
            image_array[i,j] = 255

row_sum = np.sum(image_array , axis = 1)

row_number = 0
r_break_  = 0
for i in range(image_array.shape[0]):
    if r_break_  == i:
        r_break_ += 1
        if row_sum[i] != 0:
            for j in range(i,image_array.shape[0]):
                if row_sum[j] == 0:
                    new_img = image_array[i:j, :]
                    image = Image.fromarray(new_img)
                    image.save(root_dir+'/img2/' + str(row_number) + '.png')
                    row_number += 1
                    r_break_ = j
                    break
col_number = 0
for dir in os.listdir(root_dir):
    image_file = PIL.Image.open(root_dir+dir+".png")
    image_array = np.array(image_file)

    col_sum = np.sum(image_array , axis = 0)
    
    c_break  = 0
    for i in range(image_array.shape[1]):
        if c_break == i:
            c_break += 1
            if col_sum[i] != 0:
                for j in range(i,image_array.shape[1]):
                    if col_sum[j] == 0:
                        new_img = image_array[:, i:j]
                        image = Image.fromarray(new_img)
                        image.save(root_dir+'/imgc' + str(col_number) + '.png')
                        col_number += 1
                        c_break = j
                        break
