import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import skimage.exposure as ex
import scipy.signal as sig

def show(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')

img = np.asarray(Image.open('church.jpg').convert('L'))
figure, axes = plt.subplots(2, 4, num = 'Zadanie 1.1')

mask = np.array([[0, 0, 0], [1, -1, 0], [0, 0, 0]]), \
       np.array([[0, 1, 0], [0, -1, 0], [0, 0, 0]]), \
       np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]]), \
       np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]), \
       np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]), \
       np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]), \
       np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

show('church.jpg', axes[0, :1], img)
show('church.jpg - wykrywające krawędzie 1', axes[0, 1:2], ex.equalize_hist(sig.convolve2d(img, mask[0], 'same')))
show('church.jpg - wykrywające krawędzie 2', axes[0, 2:3], ex.equalize_hist(sig.convolve2d(img, mask[1], 'same')))
show('church.jpg - wykrywające krawędzie 3', axes[0, 3:4], ex.equalize_hist(sig.convolve2d(img, mask[2], 'same')))
show('church.jpg - Prewitta 1', axes[1, :1], ex.equalize_hist(sig.convolve2d(img, mask[3], 'same')))
show('church.jpg - Prewitta 2', axes[1, 1:2], ex.equalize_hist(sig.convolve2d(img, mask[4], 'same')))
show('church.jpg - Sobela 1', axes[1, 2:3], ex.equalize_hist(sig.convolve2d(img, mask[5], 'same')))
show('church.jpg - Sobela 2', axes[1, 3:4], ex.equalize_hist(sig.convolve2d(img, mask[6], 'same')))

figure, axes = plt.subplots(2, 3, num = 'Zadanie 1.2')

sumy = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]), \
       np.array([[-2, -2, 0], [-2, 0, 2], [0, 2, 2]]), \
       np.array([[-2, -3, -2], [0, 0, 0], [2, 3, 2]]), \
       np.array([[-2, -1, 0], [-2, 0, 2], [0, 1, 2]]), \
       np.array([[-2, 0, 2], [-3, 0, 3], [-2, 0, 2]]), \
       np.array([[-2, -2, 0], [-1, 0, 1], [0, 2, 2]])

show('church.jpg - suma Prewitta', axes[0, :1], np.absolute(sig.convolve2d(img, sumy[0], 'same')))
show('church.jpg - suma Sobela', axes[0, 1:2], np.absolute(sig.convolve2d(img, sumy[1], 'same')))
show('church.jpg - Prewitta 1 + Sobela 1', axes[0, 2:3], np.absolute(sig.convolve2d(img, sumy[2], 'same')))
show('church.jpg - Prewitta 1 + Sobela 2', axes[1, :1], np.absolute(sig.convolve2d(img, sumy[3], 'same')))
show('church.jpg - Prewitta 2 + Sobela 2', axes[1, 1:2], np.absolute(sig.convolve2d(img, sumy[4], 'same')))
show('church.jpg - Prewitta 2 + Sobela 1', axes[1, 2:3], np.absolute(sig.convolve2d(img, sumy[5], 'same')))

plt.show()