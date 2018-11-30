
#实时视频图像相减运算

import cv2
import numpy as np

cap = cv2.VideoCapture('output3.avi')

Simages = []
images = []
ret,frame = cap.read()
images.append(frame)
i=0
while(ret):
    i=i+1
    ret,frame = cap.read()
    images.append(frame)
    Simage = cv2.subtract(images[i],images[0])
    Simages.append(Simage)
##    cv2.imshow("frame", frame)
##    #等待10毫秒看是否有按键输入
##    k = cv2.waitKey(10)
##    #如果输入q则退出循环
##    if k & 0xFF == ord('q'):
##        break
    ##    if cv2.waitKey(1) & 0xFF == 27:
    ##            break
print(len(Simages))
print(Simages)
cap.release()
cv2.destroyAllWindows()
