import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0,30,0,255])
plt.ion()
plt.grid()


max1=[1,1]
t=[0,0]

for i in range(30):
    image=cv2.imread("image %d.jpg"%((i+1)*50),0)
    # src=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img=image[100:150,100:150]
    max_img=img.max()
    t[0]=t[1]
    max1[0]=max1[1]
    t[1]=i
    max1[1]=max_img
    plt.plot(t,max1)
    plt.pause(0.2)



# plt.show()
# print('time=',t_max)
# print('max_value=',max1)
# print('min_value=',min1)

# plt.plot('real-time line chart')
# plt.xlabel('time')
# plt.ylabel('Pixel difference')
# plt.plot(t,max1,'r',label='maximum')
# # plt.plot(t_min,min1,'b',label='minimum')
#
# plt.legend(loc='best')
# plt.grid()
# plt.ion()
# plt.show()