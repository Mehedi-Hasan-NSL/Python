import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Plot question mark:

# img = Image.new('RGB', (500,500), (250,250,250))
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("OpenSans-Regular.ttf", 400)
# draw.text((180, -30),"?",(0,0,0),font=font)
# img.save('question_mark_img.jpg')

# plot digit numbers (from 0 to 9):
root_dir = os.path.dirname(os.path.abspath(__file__))
synth_data_path = os.path.join(root_dir,"synth_data")
for i in range(10):
    img = Image.new('RGB', (128,128), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(root_dir+"/times_new_roman.ttf", 120)
    draw.text((30, 10),str(i),(250,250,250),font=font)
    img.save(synth_data_path+'/digit_'+str(i)+'.jpg')