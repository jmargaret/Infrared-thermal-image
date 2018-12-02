import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

max1=[]
min1=[]
t_max=[]
t_min=[]
for i in range(20):
    image=cv2.imread("image %d.jpg"%((i+1)*50),0)
    # src=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img=image[100:150,100:150]
    max_img=img.max()
    max1.append(max_img)
    min_img=img.min()
    min1.append(min_img)
    t_max.append(i)
    t_min.append(i)
print('time=',t_max)
print('max_value=',max1)
print('min_value=',min1)

plt.plot('real-time line chart')
plt.xlabel('time')
plt.ylabel('Pixel difference')
plt.plot(t_max,max1,'r',label='maximum')
plt.plot(t_min,min1,'b',label='minimum')

plt.legend(loc='best')
plt.grid()
plt.ion()
plt.show()