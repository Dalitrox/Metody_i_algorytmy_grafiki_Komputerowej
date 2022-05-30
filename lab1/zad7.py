import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('lab1_gray.png')

x, y = img.shape

imgX = np.copy(img)
imgX[x//2:] = imgX[x//2-1::-1]

imgY = np.copy(img)
imgY[:,y//2:] = imgY[:, y//2::-1]

plt.subplot(1, 3, 1)
plt.imshow(img, cmap = 'gray')
plt.title('Obraz oryginalny')

plt.subplot(1, 3, 2)
plt.imshow(imgX, cmap = 'gray')
plt.title('Lustrzene odbicie górnej połowy na dolnej')

plt.subplot(1, 3, 3)
plt.imshow(imgY, cmap = 'gray')
plt.title('Lustrzane odbicie lewej połowy na prawej')

plt.show()