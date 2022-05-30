import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('lab1_gray.png')

plt.imshow(img, cmap = 'gray')
plt.title('Oryginalny obraz')

plt.figure()
img2 = np.copy(img)
m, n = img.shape

for i in range(m):
    for j in range(n):
        img2[i, j] = img[i, n - j - 1]
plt.imshow(img2, cmap = 'gray')
plt.title('Lustrzane odbicie w pionie')

plt.figure()
img3 = img[::-1]
plt.imshow(img3, cmap = 'gray')
plt.title('Lustrzane odbicie w poziomie')

plt.show()