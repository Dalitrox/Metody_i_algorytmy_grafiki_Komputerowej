import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def brightfunc(src: np.ndarray) -> float:
    size = src.shape
    return sum(map(lambda x: sum(x), src)) / (size[0] * size[1])

def contrfunc(src: np.ndarray, bright: float = None) -> float:
    if bright is None:
        bright = brightfunc(src)
    
    size = src.shape
    return (sum(map(lambda x: sum((x - bright) ** 2), src)) / (size[0] * size[1])) ** 0.5

def convert(src: np.ndarray, type_min: int, type_max: int, target_type: type) -> np.ndarray:
    imin = src.min()
    imax = src.max()

    if imin == type_min and imax == type_max:
        return src.astype(target_type)

    scale = (type_max - type_min) / (imax - imin)
    return (scale * src).astype(target_type)

def bright_contr(src: np.ndarray, info: str, name: str) -> None:

    brightness = brightfunc(src)
    contrast = contrfunc(src, brightness)
    return print(f'name: {name}, image type: {info}, brightness: {brightness}, contrast: {contrast}')

img = np.array(Image.open('lab1_gray.png'))
plt.figure('Zadanie 4')

plt.subplot(3, 2, 1)
img = convert(img, 0, 255, np.uint8)
info = img.dtype
name = 'lab1_gray.png'
plt.title(f'{name} - {info}')
plt.imshow(img, cmap = 'gray')


bright_contr(img, info, name)

plt.subplot(3, 2, 2)
img = convert(img, 0, 1, np.float64)
info = img.dtype
name = 'lab1_gray.png'
plt.title(f'{name} - {info}')
plt.imshow(img, cmap = 'gray')

bright_contr(img, info, name)

plt.subplot(3, 2, 3)
img = np.array(Image.open('gray1.bmp'))
img = convert(img, 0, 255, np.uint8)
info = img.dtype
name = 'gray1.bmp'
plt.title(f'{name} - {info}')
plt.imshow(img, cmap = 'gray')

bright_contr(img, info, name)

plt.subplot(3, 2, 4)
img = convert(img, 0, 1, np.float64)
info = img.dtype
name = 'gray1.bmp'
plt.title(f'{name} - {info}')
plt.imshow(img, cmap = 'gray')

bright_contr(img, info, name)

plt.subplot(3, 2, 5)
img = np.array(Image.open('gray2.bmp'))
img = convert(img, 0, 255, np.uint8)
info = img.dtype
name = 'gray2.bmp'
plt.title(f'{name} - {info}')
plt.imshow(img, cmap = 'gray')

bright_contr(img, info, name)

plt.subplot(3, 2, 6)
img = convert(img, 0, 1, np.float64)
info = img.dtype
name = 'gray2.bmp'
plt.title(f'{name} - {info}')
plt.imshow(img, cmap = 'gray')

bright_contr(img, info, name)

plt.show()