from bs4 import *
import requests
import os, os.path
from PIL import Image


root_dir = os.path.dirname(os.path.abspath(__file__))

# change your input size
input_no_images = 3

# CREATE FOLDER
def folder_create(images):
    #path = os.getcwd()
    #folder_name = path
    path = os.mkdir(os.path.join(root_dir,'images'))
    download_images(images, path)
  
  
def download_images(images, folder_name):
    count = 0
    print(f"Total {len(images)} Image Found!")
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass

            try:
                r = requests.get(image_link).content
                try:
  
                    r = str(r, 'utf-8')
  
                except UnicodeDecodeError:
  
                    with open(f"{folder_name}/images{i+1}", "wb+") as f:
                        f.write(r)
                    count += 1
            except:
                pass
  
        if count == len(images):
            print("All Images Downloaded!")

        #################### part2
        if count < input_no_images:
            print("WE found {} less than input no of images".format(count-input_no_images))
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")
  

def resize_image():
    imgs = []
    image_dir = '/images'
    path = root_dir + image_dir
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(path,f)))
    
    pr_path = os.makedirs(os.path.join(root_dir,'preprocessed'), exist_ok=True)
    for img in imgs:
        new_img = img.resize((224,224))
        new_img.save(pr_path)
    print("All image resized")

def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')
    folder_create(images)
    resize_image()
  
  
url = "https://www.prothomalo.com/"
  
main(url)