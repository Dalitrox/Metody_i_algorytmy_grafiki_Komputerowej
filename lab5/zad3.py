import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import skimage.exposure as ex
import scipy.signal as sig

def show(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')

img = np.asarray(Image.open('Lenna.jpg').convert('L'))
figure, axes = plt.subplots(1, 4, num = 'Zadanie 3')

mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]), \
       np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]), \
       np.array([[-1, -2, -1], [-2, 13, -2], [-1, -2, -1]])

show('Lenna.jpg', axes[0:1], img)
show('Lenna.jpg - filtr wyostrzający 1', axes[1:2], ex.equalize_hist(sig.convolve2d(img, mask[0], 'same')))
show('Lenna.jpg - filtr wyostrzający 2', axes[2:3], ex.equalize_hist(sig.convolve2d(img, mask[1], 'same')))
show('Lenna.jpg - filtr wyostrzający 3', axes[3:4], ex.equalize_hist(sig.convolve2d(img, mask[2], 'same')))

plt.show()