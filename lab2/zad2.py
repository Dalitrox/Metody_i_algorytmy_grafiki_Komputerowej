import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('obraz1.jpg'))
img2 = np.array(Image.open('obraz2.jpg').resize(img.shape[1::-1])) # dokonuje skalowania tego obrazu do wymiarów obrazu pierwszego
img3 = np.array(Image.open('obraz3.jpg').resize(img.shape[1::-1])) # dokonuje skalowania tego obrazu do wymiarów obrazu pierwszego

plt.figure('Zadanie 2')

plt.subplot(1, 4, 1)
plt.title('Obraz 1')
plt.imshow(img)

plt.subplot(1, 4, 2)
plt.title('Obraz 2')
plt.imshow(img2)

plt.subplot(1, 4, 3)
plt.title('Obraz 3')
plt.imshow(img3)

plt.subplot(1, 4, 4)
plt.title('Obraz wynikowy')
images = (img * 0.33 + img2 * 0.33 + img3 * 0.34).astype(np.uint8)
plt.imshow(images)

plt.show()