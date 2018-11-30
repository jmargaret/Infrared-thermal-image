import cv2
video=cv2.VideoCapture('output3.avi')
s=1
if video.isOpened():
    ravel,frame = video.read()
else:
    ravel=False

time=50
while ravel:
    ravel,frame =video.read()
    # print('read a frame:'),ravel

    # array=[]
    # array.append(1)
    if(s%time==0):
        cv2.imwrite("image "+str(s)+'.jpg',frame)
    s+=1
    cv2.waitKey(10)
video.release()
