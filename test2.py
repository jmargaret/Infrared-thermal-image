from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import cv2
from matplotlib import pyplot as plt

fig=plt.figure()
ax=fig.gca(projection='3d')
# ax=fig.add_subplot(111,projection='3d')
# plt.show()

image = cv2.imread('image 50.jpg')
img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(img)