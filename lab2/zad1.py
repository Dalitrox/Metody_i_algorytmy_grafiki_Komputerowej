import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

img = np.array(Image.open('lab1_gray.png'))
plt.figure('Zadanie 1')

plt.subplot(1, 2, 1)
plt.imshow(img, cmap = 'gray')
plt.title('Oryginalny obraz')

if img.dtype == np.uint8:
    img2 = 255 - img[:,:]
else:
    img2 = 1 - img[:,:]

plt.subplot(1, 2, 2)
plt.imshow(img2, cmap = 'gray')
plt.title('Obraz w negatywie')

plt.show()