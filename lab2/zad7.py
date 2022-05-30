import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = np.array(Image.open('lab1_gray.png'))
plt.figure('Zadanie 7')

plt.subplot(1, 3, 1)
plt.title('Obraz oryginalny')
plt.imshow(img, cmap = 'gray')

plt.subplot(1, 3, 2)
plt.title('Gamma: 0.5')
img2 = np.copy(img)
img2 = np.array(255 * (img2 / 255) ** 2, dtype = 'uint8')
plt.imshow(img2, cmap = 'gray')

plt.subplot(1, 3, 3)
plt.title('Gamma: 2')
img3 = np.copy(img)
img3 = np.array(255 * (img3 / 255) ** 0.5, dtype = 'uint8')
plt.imshow(img3, cmap = 'gray')

plt.show()