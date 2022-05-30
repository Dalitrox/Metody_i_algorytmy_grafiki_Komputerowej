import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def salt_and_pepper(src: np.ndarray, proc: int) -> np.ndarray:
    procent = proc / 100
    sprandom = np.random.rand(*src.shape)

    src[sprandom < procent] = 0
    src[sprandom > 1 - procent] = 255

    return src

def median(src: np.ndarray, size: int) -> np.ndarray:
    w, h = src.shape
    shape = size // 2

    tmp = np.zeros((w + 2 * shape, h + 2 * shape), dtype = np.float64)
    tmp[shape:shape + w, shape: shape + h] = src.copy().astype(np.float64)

    dst = tmp.copy()

    for x in range(w):
        for y in range(h):
            dst[x + shape, y + shape] = np.median(tmp[x:x + size, y:y + size])

    dst = dst[shape:shape + w, shape: shape + h].astype(np.uint8)
    return dst

def show(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap='gray')

img = salt_and_pepper(np.asarray(Image.open('clown.gif').convert('L')), 5)

figure, axes = plt.subplots(1, 4, num = 'Zadanie 3')

show('clown.gif', axes[:1], img)
show('clown.gif - 3x3', axes[1:2], median(img, 3))
show('clown.gif - 5x5', axes[2:3], median(img, 5))
show('clown.gif - 7x7', axes[3:4], median(img, 7))

plt.show()