from PIL import Image
import cv2
import numpy as np
import matplotlib as plt
from pyecharts import Bar3D

src_1=cv2.imread("image 900.jpg")
src_2=cv2.imread("image 1000.jpg")
src1=cv2.cvtColor(src_1,cv2.COLOR_BGR2GRAY)
src2=cv2.cvtColor(src_2,cv2.COLOR_BGR2GRAY)
img1=src1[100:110,100:110]
img2=src2[100:110,100:110]
sub=cv2.subtract(img2,img1)
im=Image.fromarray(sub)
im.save('out.jpg')
s=np.reshape(sub,[1,10*10])
s=s[0]
print(type(s))
s1=[]
for k in s:
    s1.append(k)
print(s)
image=cv2.imread('out.jpg')
img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# print(img)
m,n=img.shape
x=np.arange(0,m)
x1=[]
y=np.arange(0,n)
s2=[]
# for i in x:
#     x1.append(i)
# print(x1)
# for k in s:
#     s2.append(k)
# print(s2)
for i in x:
    for j in y:
        for k in s:
            s2.append(i)