import numpy as np
from PIL import Image

def ft_invert(array) -> np.ndarray:
    """
    Invert the colors of the image represented by the 3D numpy array.
    :param array: 3D numpy array representing the image.
    :return: 3D numpy array with inverted colors.
    """
    inverted = 255 - array
    img = Image.fromarray(inverted.astype(np.uint8))
    img.show()
    return inverted

def ft_red(array) -> np.ndarray:
    """
    Extract the red channel from the image represented by the 3D numpy array.
    :param array: 3D numpy array representing the image.
    :return: 3D numpy array with only the red channel.
    """
    red = array * [1, 0, 0]
    img = Image.fromarray(red.astype(np.uint8))
    img.show()
    return red

def ft_green(array) -> np.ndarray:
    """
    Extract the green channel from the image represented by the 3D numpy array.
    :param array: 3D numpy array representing the image.
    :return: 3D numpy array with only the green channel.
    """
    green = np.copy(array)
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    img = Image.fromarray(green.astype(np.uint8))
    img.show()
    return green

def ft_blue(array) -> np.ndarray:
    """
    Extract the blue channel from the image represented by the 3D numpy array.
    :param array: 3D numpy array representing the image.
    :return: 3D numpy array with only the blue channel.
    """
    shape = array.shape
    blue = np.zeros(shape, dtype=np.uint8)
    blue[:, :, 2] = array[:, :, 2]
    img = Image.fromarray(blue)
    img.show()
    return blue

def ft_grey(array) -> np.ndarray:
    """
    Convert the image represented by the 3D numpy array to grayscale.
    :param array: 3D numpy array representing the image.
    :return: 3D numpy array representing the grayscale image.
    """
    img = Image.fromarray(array)
    img = img.convert("L")
    img.show()
    grey_image = np.array(img)
    return grey_image
