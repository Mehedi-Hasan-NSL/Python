import numpy as np
from PIL import Image
from PIL import ImageOps
import os 
import cv2

root_dir = os.path.dirname(os.path.abspath(__file__))

img = Image.open(root_dir+ '/E1.png')
img = ImageOps.grayscale(img)

img = np.array(img)

#inverting the image
img = 255. - img 

img_mean = np.mean(img)
row_sum = np.sum(img , axis=1)

# checking rowwise sum for the text and append them on list

j = 0
img_list = []
for i in range(1, img.shape[0]):
    if row_sum[i] == 0:
        img_list.append(img[j:i,:])
        j=i
img_list.append(img[j:, :])
    
#print(len(img_list))

## spliting row texts
img_list2 = []
cnt = 0
j=0
for i in range(len(img_list)):
    if np.sum(img_list[i]) != 0:
        cv2.imwrite(root_dir+'/'+str(cnt)+'.jpg', img_list[i])
        row_image = Image.fromarray(img_list[i])
        row_image= row_image.convert('RGB')
        row_image.save('img.png')
        img_list2.append(img_list[i])

        cnt+=1


## for characters
print("textline segmented on the current working directory")
j = 0

# col_sum = np.sum(img_list , axis = 0)
# image_cols = []
# for i in range(1, image_array.shape[1]):
#     if col_sum[i] == 0:
#         image_cols.append(image_array[:, j:i])
#         j=i
# image_cols.append(image_array[:, j:])
# for i in range(len(image_cols)):
#     if np.sum(image_cols[i]) != 0:
#         image = Image.fromarray(image_cols[i])
#         image = image.convert('RGB')
#         image.save('img' + str(row_number) + '.png')
#         #print(np.array(image))
#         col_number += 1