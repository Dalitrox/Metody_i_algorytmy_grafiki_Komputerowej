import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from skimage.exposure import equalize_hist

def equalization(src: np.ndarray) -> np.ndarray:
    size = src.shape

    tmp = np.asarray([np.size(src[src <= x]) for x in range(256)])
    trans_map = (255 * tmp) // (size[0] * size[1])

    return trans_map[src]

def hist(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')
    axes[1].set_title(f'{title} - histogram')
    axes[1].hist(src.flatten(), bins = 256)
    axes[1].set_xlim(0, 255)

img = np.asarray(Image.open('hist_gray.jpg')), np.asarray(Image.open('hist_couple.bmp'))
figure, axes = plt.subplots(2, 6, num = 'Zadanie 6')

hist('hist_gray.jpg', axes[0, :2], img[0])
hist('hist_gray.jpg - gotowa funkcja', axes[0, 2:4], np.asarray(equalize_hist(img[0]) * 255, dtype = np.uint8))
hist('hist_gray.jpg - własna funkcja', axes[0, 4:], equalization(img[0]))
hist('hist_couple.bmp', axes[1, :2], img[1])
hist('hist_couple.bmp - gotowa funkcja', axes[1, 2:4], np.asarray(equalize_hist(img[1]) * 255, dtype = np.uint8))
hist('hist_couple.bmp - własna funkcja', axes[1, 4:], equalization(img[1]))

plt.show()