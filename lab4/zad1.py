import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from typing import Callable

def filters(src: np.ndarray, size: int, function: Callable[[np.ndarray], int]) -> np.ndarray:
    tmp = src.copy()

    shape = src.shape
    for i in range(shape[0] - size // 2):
        for j in range(shape[1] - size // 2):
            tmp[i + size // 2, j + size // 2] = function(src[i:i + size, j:j + size])

    return tmp

def show(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')

img = np.asarray(Image.open('clown.gif').convert('L'))
size = 3
figure, axes = plt.subplots(2, 4, num = 'Zadanie 1')

show('clown.gif', axes[0, :1], img)
show('clown.gif - min 3x3', axes[0, 1:2], filters(img, 3, np.min))
show('clown.gif - min 5x5', axes[0, 2:3], filters(img, 5, np.min))
show('clown.gif - min 7x7', axes[0, 3:4], filters(img, 7, np.min))
show('clown.gif', axes[1, :1], img)
show('clown.gif - max 3x3', axes[1, 1:2], filters(img, 3, np.max))
show('clown.gif - max 5x5', axes[1, 2:3], filters(img, 5, np.max))
show('clown.gif - max 7x7', axes[1, 3:4], filters(img, 7, np.max))

plt.show()