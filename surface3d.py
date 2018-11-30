import cv2
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from PIL import Image

fig = plt.figure()
ax = fig.gca(projection='3d')

image = cv2.imread('image 50_output.jpg')

# if len(img.shape) > 2:

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# img = Image.open("image 50.jpg")
# box1 = (200, 390, 210, 400)    #设置图像裁剪区域
# image1 = img.crop(box1)
# image2 = image1.save('image50_output.jpg')
# # Make data.
# img1 = cv2.imread('image50_output.jpg')
m, n = img.shape
X = np.arange(0,m, 1)
plt.xlabel('X')
Y = np.arange(0,n, 1)
plt.ylabel('Y')
X, Y = np.meshgrid(X, Y)
Z = np.array(img)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0,255)
ax.set_label('gray scale')
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
