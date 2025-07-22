from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def transpose_image(matrix: list[list[int]]) -> list[list[int]]:
    """
    transpose the image.
    """
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        transposed.append(new_row)
    return transposed


def main():
    """
    this is a program that loads an image, zooms in on it\
by cropping the center,
    converts the zoomed image to grayscale, and then transposes it.
    It displays the transposed grayscale image.
    It also prints the shape of the image before and after transposing.
    """

    path = "animal.jpeg"
    img = ft_load(path)

    try:
        assert isinstance(img, Image.Image), \
            "The loaded object is not a PIL Image."
        assert img.mode == 'RGB', \
            "The image must be in RGB mode."
        assert img.size[0] >= 400 and img.size[1] >= 400, \
            "The image must be at least 400x400 pixels."

        width, height = img.size
        center_x, center_y = width // 2, height // 2
        
        zoomed_img = img.crop((450, 100, 850, 500))
        gray_zoomed = zoomed_img.convert("L")
        zoomed_array = np.array(gray_zoomed)
        zoomed_array = np.expand_dims(zoomed_array, axis=-1)
        print(f"The shape of image is: {zoomed_array.shape}\
or {zoomed_img.size}")
        print(zoomed_array)

        transpose = transpose_image(zoomed_array.tolist())
        transposed_array = np.array(transpose)
        print(f"New shape after Transpose: {transposed_array.shape[:2]}")
        print(transposed_array)

        plt.imshow(transposed_array, cmap='gray')
        plt.title("transposed Image")
        plt.axis('on')
        plt.show()
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
