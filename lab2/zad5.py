import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('lab1_gray.png'))
plt.figure('Zadanie 5')

# stałe dla obrazu monochromatycznego
brightnessInc = 80
brightnessDec = -40
contrstHigh = 1.7
contrastLow = 0.05

# stałe dla obrazu kolorowego
brightnessIncRGB = 30
brightnessDecRGB = -45
contrstHighRGB = 1.5
contrastLowRGB = 0.5

plt.subplot(3, 5, 1)
plt.title('Obraz monochromatyczny oryginalny')
plt.imshow(img, cmap = 'gray')

plt.subplot(3, 5, 2)
plt.title('Obraz monochrom jasność +80')
img2 = np.copy(img)
img2 = np.clip(img2 + float(brightnessInc), 0, 255).astype(np.uint8)
plt.imshow(img2, cmap = 'gray')

plt.subplot(3, 5, 3)
plt.title('Obraz monochrom. jasność -40')
img3 = np.copy(img)
img3 = np.clip(img3 + float(brightnessDec), 0, 255).astype(np.uint8)
plt.imshow(img3, cmap = 'gray')

plt.subplot(3, 5, 4)
plt.title('Obraz monochrom. kontrast 1.7')
img4 = np.copy(img)
img4 = np.clip(img4 * float(contrstHigh), 0, 255).astype(np.uint8)
plt.imshow(img4, cmap = 'gray')

plt.subplot(3, 5, 5)
plt.title('Obraz monochrom. kontrast 0.05')
img5 = np.copy(img)
img5 = np.clip(img5 * float(contrastLow), 0, 255).astype(np.uint8)
plt.imshow(img5, cmap = 'gray')

plt.subplot(3, 5, 6)
plt.title('Obraz RGB oryginalny')
imgC = np.array(Image.open('raz.jpg'))
plt.imshow(imgC)

plt.subplot(3, 5, 7)
plt.title('Obraz RGB jasność +30')
imgC2 = np.copy(imgC)
imgC2 = np.clip(imgC2 + float(brightnessIncRGB), 0, 255).astype(np.uint8)
plt.imshow(imgC2)

plt.subplot(3, 5, 8)
plt.title('Obraz RGB jasność -45')
imgC3 = np.copy(imgC)
imgC3 = np.clip(imgC3 + float(brightnessDecRGB), 0, 255).astype(np.uint8)
plt.imshow(imgC3)

plt.subplot(3, 5, 9)
plt.title('Obraz RGB kontrast 1.5')
imgC4 = np.copy(imgC)
imgC4 = np.clip(imgC4 * float(contrstHighRGB), 0, 255).astype(np.uint8)
plt.imshow(imgC4)

plt.subplot(3, 5, 10)
plt.title('Obraz RGB kontrast 0.5')
imgC5 = np.copy(imgC)
imgC5 = np.clip(imgC5 * float(contrastLowRGB), 0, 255).astype(np.uint8)
plt.imshow(imgC5)

plt.subplot(3, 5, 11)
plt.title('Obraz RGB oryginalny')
imgC = np.array(Image.open('obraz3.jpg'))
plt.imshow(imgC)

plt.subplot(3, 5, 12)
plt.title('Obraz RGB jasność +30')
imgC2 = np.copy(imgC)
imgC2 = np.clip(imgC2 + float(brightnessIncRGB), 0, 255).astype(np.uint8)
plt.imshow(imgC2)

plt.subplot(3, 5, 13)
plt.title('Obraz RGB jasność -45')
imgC3 = np.copy(imgC)
imgC3 = np.clip(imgC3 + float(brightnessDecRGB), 0, 255).astype(np.uint8)
plt.imshow(imgC3)

plt.subplot(3, 5, 14)
plt.title('Obraz RGB kontrast 1.5')
imgC4 = np.copy(imgC)
imgC4 = np.clip(imgC4 * float(contrstHighRGB), 0, 255).astype(np.uint8)
plt.imshow(imgC4)

plt.subplot(3, 5, 15)
plt.title('Obraz RGB kontrast 0.5')
imgC5 = np.copy(imgC)
imgC5 = np.clip(imgC5 * float(contrastLowRGB), 0, 255).astype(np.uint8)
plt.imshow(imgC5)

plt.show()