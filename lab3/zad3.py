import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from skimage.exposure import equalize_hist

def hist(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')
    axes[1].set_title(f'{title} - histogram')
    axes[1].hist(src.flatten(), bins = 256)
    axes[1].set_xlim(0, 255)

img = np.asarray(Image.open('hist_gray.jpg')), np.asarray(Image.open('hist_couple.bmp'))

figure, axes = plt.subplots(2, 4, num = 'Zadanie 3')

hist('hist_gray.jpg', axes[0, :2], img[0])
hist('hist_gray.jpg - wyrównany', axes[0, 2:4], np.asarray(equalize_hist(img[0]) * 255, dtype = np.uint8))
hist('hist_couple.bmp', axes[1, :2], img[1])
hist('hist_couple.bmp - wyrównany', axes[1, 2:4], np.asarray(equalize_hist(img[1]) * 255, dtype = np.uint8))

plt.show()