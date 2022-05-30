import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def salt_and_pepper(src: np.ndarray, proc: int) -> np.ndarray:
    procent = proc / 100
    sprandom = np.random.rand(*src.shape)

    src[sprandom < procent] = 0
    src[sprandom > 1 - procent] = 255

    return src

def show(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')

img = np.asarray(Image.open('clown.gif').convert('L'))

figure, axes = plt.subplots(1, 2, num = 'Zadanie 2')

show('clown.gif', axes[:1], img)
show('clown.gif - szum', axes[1:2], salt_and_pepper(img, 5))

plt.show()