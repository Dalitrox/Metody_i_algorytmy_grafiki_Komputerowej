import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('lab1_gray.png')

plt.imshow(img, cmap = 'gray')
plt.title('Oryginalny obraz')

plt.figure()
img2 = img[99:299, 349:549]
plt.imshow(img2, cmap = 'gray')
plt.title('Wycięty fragment')

plt.show()