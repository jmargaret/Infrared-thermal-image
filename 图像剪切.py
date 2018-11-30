import cv2
import numpy as np
from PIL import Image
img = Image.open("image 50.jpg")
box1 = (200, 0, 600, 400)    #设置图像裁剪区域
image1 = img.crop(box1)
image2 = image1.save('image 50_output.jpg')