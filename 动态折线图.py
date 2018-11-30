import numpy as np
import matplotlib.pyplot as plt
import cv2
plt.axis([0, 100, 0, 255])
plt.ion()


video=cv2.VideoCapture('output3.avi')
s=1
if video.isOpened():
    ravel,frame = video.read()
else:
    ravel=False

time=50
while ravel:
    ravel,frame =video.read()
    if(s%time==0):
        cv2.imwrite("image "+str(s)+'.jpg',frame)

    s+=1
    cv2.waitKey(10)
video.release()
xs = [0, 0]
ys = [1, 1]
for i in range(50,1800):
    image = cv2.imread('E:\江江\新实验\image .jpg', 0)
image = cv2.imread('image 50.jpg',0)
img= image[200:150, 210:160]
m,n=img.shape
# x=np.arange(0,m)
# y=np.arange(0,n)
fo
for i in range(100):
    y = np.random.random()
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = y
    plt.plot(xs, ys)
    plt.pause(0.1)