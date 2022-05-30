import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def salt_and_pepper(src: np.ndarray, proc: int) -> np.ndarray:
    procent = proc / 100
    sprandom = np.random.rand(*src.shape)

    src[sprandom < procent] = 0
    src[sprandom > 1 - procent] = 255

    return src

def enlarge(src: np.ndarray, size: int) -> np.ndarray:
    scale = (size // 2, 1)
    tmp = src.copy()

    tmp = np.vstack((np.tile(tmp[0, :], scale), tmp))
    tmp = np.vstack((tmp, np.tile(tmp[-1, :], scale)))
    tmp = np.hstack((np.tile(tmp[:, 0], scale).T, tmp))
    tmp = np.hstack((tmp, np.tile(tmp[:, -1], scale).T))

    return tmp

def median(src: np.ndarray, size: int) -> np.ndarray:
    bigger_img = enlarge(src, size)
    copy = bigger_img.copy()
    dst = size // 2
    shape = bigger_img.shape

    for i in range(shape[0] - dst):
        for j in range(shape[1] - dst):
            median = np.median(bigger_img[i:i + size, j:j + size])
            copy[i + dst, j + dst] = median

    return copy[dst:shape[0] - dst, dst:shape[1] - dst]

def show(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')

img = salt_and_pepper(np.asarray(Image.open('clown.gif').convert('L')), 10)
figure, axes = plt.subplots(1, 4, num='Zadanie 4')

show('clown.gif', axes[:1], img)
show('clown.gif - median 3x3', axes[1:2], median(img, 3))
show('clown.gif - median 5x5', axes[2:3], median(img, 5))
show('clown.gif - median 7x7', axes[3:4], median(img, 7))

plt.show()