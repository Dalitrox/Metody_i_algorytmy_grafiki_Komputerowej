import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('lab1_color.png')

x, y, z = img.shape

img2 = np.zeros([x, y*2, z])
img2[:x, :y] = img
img2[:x, y:] = img[:,::-1]

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Obraz oryginalny')

plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.title('Lustrzane odbicia sklejonego obrazu')

plt.show()