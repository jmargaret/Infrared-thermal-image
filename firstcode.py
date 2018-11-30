import cv2
import time
import os
import numpy as np
from PIL import Image

cap = cv2.VideoCapture('D:\python code\image\output3.avi')

ok,frame = cap.read()
i = 1
j = 0
while(ok):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('D:/gray.jpg',gray)
    img = Image.open("D:/gray.jpg")
    box1 = (200, 10, 500, 400)    #设置图像裁剪区域
    image1 = img.crop(box1)   #图像裁剪
    image1.save('D:/python code/result/{}.jpg'.format(i))  #存储当前区域
    image = cv2.imread('D:/python code/result/{}.jpg'.format(i))
    im_color = cv2.applyColorMap(image, 2)
    cv2.imwrite("D:/python code/result/{}-1.jpg".format(i), im_color)
    cv2.imshow('colorimgage',im_color)
    cv2.imshow('origeimgage',image)
    i = i+1
    while(ok):
        ok,frame = cap.read()
        j = j+1
        if(j==300):
            j=0
            break

     #等待10毫秒看是否有按键输入
    k = cv2.waitKey(10)
    #如果输入q则退出循环
    if k & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
