import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('raz.jpg')

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title('Oryginalny obraz')

plt.subplot(2, 2, 2)
plt.imshow(img[:, :, 0], cmap = 'gray')
plt.title('Kanał czerwony')

plt.subplot(2, 2, 3)
plt.imshow(img[:, :, 1], cmap = 'gray')
plt.title('Kanał zielony')

plt.subplot(2, 2, 4)
plt.imshow(img[:, :, 2], cmap = 'gray')
plt.title('Kanał niebieski')

plt.show()