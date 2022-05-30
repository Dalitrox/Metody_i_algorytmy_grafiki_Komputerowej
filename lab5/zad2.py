import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import skimage.exposure as ex
import scipy.signal as sig

def show(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')

img = np.asarray(Image.open('Airplane24.jpg').convert('L'))
figure, axes = plt.subplots(1, 4, num = 'Zadanie 2')

mask = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]), \
       np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]), \
       np.array([[-1, -2, -1], [-2, 12, -2], [-1, -2, -1]])

show('Airplane24.jpg', axes[0:1], img)
show('Airplane24.jpg - filtr konturowy 1', axes[1:2], ex.equalize_hist(sig.convolve2d(img, mask[0], 'same')))
show('Airplane24.jpg - filtr konturowy 2', axes[2:3], ex.equalize_hist(sig.convolve2d(img, mask[1], 'same')))
show('Airplane24.jpg - filtr konturowy 3', axes[3:4], ex.equalize_hist(sig.convolve2d(img, mask[2], 'same')))

plt.show()