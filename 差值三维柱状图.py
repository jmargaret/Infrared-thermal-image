from PIL import Image
import cv2
import numpy as np
import matplotlib as plt
from pyecharts import Bar3D

src_1=cv2.imread("image 900.jpg")
src_2=cv2.imread("image 1000.jpg")
src1=cv2.cvtColor(src_1,cv2.COLOR_BGR2GRAY)
src2=cv2.cvtColor(src_2,cv2.COLOR_BGR2GRAY)
img1=src1[100:150,100:150]
img2=src2[100:150,100:150]
sub=cv2.subtract(img2,img1)
im=Image.fromarray(sub)
im.save('out.jpg')
s=np.reshape(sub,[1,50*50])
s=s[0]
s1=[]
for k in s:
    s1.append(k)
print(s)
# x_axis=[]
# y_axis=[]

image=cv2.imread('out.jpg')
img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# print(img)
m,n=img.shape

x=np.arange(0,m)
print('x=',x)
x1=[]
for i in x:
    x1.append(i)
print('x1=',x1)

y=np.arange(0,n)
print('y=',y)
y1=[]
for j in y:
    y1.append(j)
print('y1=',y1)

s2=[]
for i in x:
    for j in y:
        temp=[]
        temp.append(i)
        temp.append(j)
        temp.append(img[i,j])
        s2.append(temp)
s3=np.array(s2,dtype='uint8')
print('s3=',s3)


bar3d=Bar3D('帧差值三维柱状图', width=1000, height=1000)
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x, y,  [[d[0], d[1], d[2]] for d in s3],
          is_visualmap=True, visual_range=[0, 10],
          visual_range_color=range_color,
          grid3d_width=100, grid3d_depth=100,
          grid3d_shading='lambert',             #柱状图显示更真实（可省略）
          is_grid3d_rotate=True,                #自动旋转（可省略）
          grid3d_rotate_speed=10)               #旋转速度（可省略）
bar3d.render()
