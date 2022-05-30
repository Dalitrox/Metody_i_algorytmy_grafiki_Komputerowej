import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from skimage.exposure import rescale_intensity

def stretch(src: np.ndarray, imin: int = None, imax: int = None) -> np.ndarray:
    imin = np.min(src)
    imax = np.max(src)

    tmp = src.copy()
    tmp[tmp < imin] = 0
    tmp[tmp > imax] = 255

    tmp = (tmp - imin) / (imax - imin)

    return np.asarray(255 * tmp, dtype = np.uint8)

def hist(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')
    axes[1].set_title(f'{title} - histogram')
    axes[1].hist(src.flatten(), bins = 256)
    axes[1].set_xlim(0, 255)

img = np.asarray(Image.open('hist_gray.jpg')), np.asarray(Image.open('hist_couple.bmp'))
figure, axes = plt.subplots(2, 6, num = 'Zadanie 5')

hist('hist_gray.jpg', axes[0, :2], img[0])
hist('hist_gray.jpg - gotowa funkcja', axes[0, 2:4], rescale_intensity(img[0]))
hist('hist_gray.jpg - własna funkcja', axes[0, 4:], stretch(img[0]))
hist('hist_couple.bmp', axes[1, :2], img[1])
hist('hist_couple.bmp - gotowa funkcja', axes[1, 2:4], rescale_intensity(img[1]))
hist('hist_couple.bmp - własna funkcja', axes[1, 4:], stretch(img[1]))

plt.show()