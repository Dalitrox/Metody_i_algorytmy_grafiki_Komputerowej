import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('lab1_color.png')

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Oryginalny obraz')

img2 = img[49:199, 99:176]
plt.imsave('lab1_color_2.jpg', img2)

plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.title('Wycięty fragment')

plt.show()