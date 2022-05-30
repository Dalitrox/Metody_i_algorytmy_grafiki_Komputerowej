import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def get_hist(src: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

    h = np.zeros(255)

    for i in src:
        for j in i:
            h[j] += 1

    return np.arange(255), h

def hist(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')
    axes[1].set_title(f'{title} - hitogram funkcja hist')
    axes[1].hist(src.flatten(), bins = 256)
    axes[1].set_xlim(0, 255)
    axes[2].set_title(f'{title} - histogram ręczny')
    axes[2].bar(*get_hist(src), width = 0.6)
    axes[2].set_xlim(0, 255)

img = np.asarray(Image.open('hist_gray.jpg'))

figure, axes = plt.subplots(1, 3, num = 'Zadanie 4')

hist('hist_gray.jpg', axes, img)

plt.show()