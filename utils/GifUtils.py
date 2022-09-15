import imageio
from PIL import Image
import os

def preProcess(image_list):
    """处理一下图片大小"""
    if not os.path.exists("static/tmp/"):
        os.makedirs("static/tmp/")
    for image_name in image_list:
        im = Image.open(image_name)
        im = im.resize((300, 300))  # 都搞成(100,100)尺寸的
        im.save("static/tmp/"+str(image_list.index(image_name))+".png",False)  # False指的是覆盖掉之前尺寸不规范的图片

def create_gif(image_list, gif_name, duration=1):
    """制作gif图"""
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)  # 选择'GIF'类型

def merge(upImg,downImg,outputImgFolder):
    for up,down in zip(upImg,downImg):
        im1 = Image.open(up)
        r, g, b, a = im1.split()
        im2 = Image.open(down)
        im = Image.composite(im1, im2, a)
        im.save(outputImgFolder+str(downImg.index(down))+".jpg")
