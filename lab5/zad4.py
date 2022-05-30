import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import skimage.exposure as ex

def enlarge(src: np.ndarray, mask_shape: tuple[int, int]) -> np.ndarray:
    board_x = mask_shape[0] // 2
    board_y = mask_shape[1] // 2
    return np.pad(src, ((board_x, board_y), (board_x, board_y)), "edge")

def conv(src: np.ndarray, mask: np.ndarray) -> np.ndarray:
    m_shape = mask.shape
    bigger = enlarge(src, m_shape)
    tmp = np.zeros_like(src, dtype = np.int16)
    for x in range(src.shape[1]):
        for y in range(src.shape[0]):
            tmp[y, x] = (mask * bigger[y:y + 3, x:x + 3]).sum()
    return ex.equalize_hist(tmp)

def show(title: str, axes: plt.Axes, src: np.ndarray) -> None:
    axes[0].set_title(title)
    axes[0].imshow(src, cmap = 'gray')

img = np.asarray(Image.open('Lenna.jpg').convert('L'))
figure, axes = plt.subplots(1, 4, num = 'Zadanie 4')

mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]), \
       np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]), \
       np.array([[-1, -2, -1], [-2, 13, -2], [-1, -2, -1]])

show('Lenna.jpg', axes[0:1], img)
show('Lenna - filtr wyostrzający 1', axes[1:2], conv(img, mask[0]))
show('Lenna - filtr wyostrzający 2', axes[2:3], conv(img, mask[1]))
show('Lenna - filtr wyostrzający 3', axes[3:4], conv(img, mask[2]))

plt.show()