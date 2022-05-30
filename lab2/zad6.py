import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('lab1_gray.png')).astype(np.uint8)
plt.figure('Zadanie 6')

plt.subplot(1, 2, 1)
plt.title('Obraz oryginalny')
plt.imshow(img, cmap = 'gray')

plt.subplot(1, 2, 2)
img2 = np.copy(img)
x, y = np.array(img2).shape
plt.title('Po zamianie wartości')
im = np.copy(img2)

im[im > 192] = 255

for i in range(x):
    for j in range(y):
        if im[i, j] < 64:
            im[i, j] = 0

plt.imshow(im, cmap = 'gray')

plt.show()