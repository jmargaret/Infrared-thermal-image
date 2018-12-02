import cv2
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter


fig=plt.figure()
ax=fig.gca(projection='3d')
# ax=fig.add_subplot(111,projection='3d')
# plt.show()

image = cv2.imread('image 50.jpg',0)
img= image[200:150, 210:160]
m,n=img.shape
x=np.arange(0,m,1)
y=np.arange(0,n,1)
# x=np.arange(200,210,1)
# y=np.arange(150,160,1)
x,y=np.meshgrid(x,y)

# for i in range(200,210):
#     for j in range(150,160):
z=img[x,y]


surface=ax.plot_surface(x,y,z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,255)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(ax.FormatStrFormatter('%.02f'))
fig.colorbar(surface,shrink=0.5,aspect=5)
plt.show()