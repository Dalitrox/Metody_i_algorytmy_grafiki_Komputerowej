import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('lab1_gray.png'))
plt.figure('Zadanie 3')

plt.subplot(1, 5, 1)
plt.title('Obraz oryginalny')
plt.imshow(img, cmap = 'gray')

plt.subplot(1, 5, 2)
plt.title('Obrót o 90 stopni w lewo')
img2 = np.rot90(img)
plt.imshow(img2, cmap = 'gray')

plt.subplot(1, 5, 3)
plt.title('Obrót o 90 stopni w prawo')
img3 = np.rot90(img, -1)
plt.imshow(img3, cmap = 'gray')

plt.subplot(1, 5, 4)
plt.title('Transpozycja obrazu')
img4 = np.transpose(img)
plt.imshow(img4, cmap = 'gray')

plt.subplot(1, 5, 5)
plt.title('Obrót o 90 stopni w prawo w pętli')
x, y = img.shape

img5 = np.zeros([y, x], dtype = np.double)

for i in range(x):
    for j in range(y):
        img5[j, x - i - 1] = img[i, j]

plt.imshow(img5, cmap = 'gray')

plt.show()