import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('raz.jpg')

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Oryginalny obraz')

plt.subplot(1, 2, 2)
img2 = np.copy(img)
img2[:, :, 0] = img[:, :, 2]
img2[:, :, 2] = img[:, :, 0]
plt.imshow(img2)
plt.title('Obraz po zamianie kanałów')

plt.show()