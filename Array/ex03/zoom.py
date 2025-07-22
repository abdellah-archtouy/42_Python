from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def main():
    """
    This function loads an image, zooms in on it\
by cropping the center,
    and converts the zoomed image to grayscale.
    It then displays the zoomed grayscale image.
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

        zoomed_img = img.crop((450, 100, 850, 500))
        gray_zoomed = zoomed_img.convert("L")
        zoomed_array = np.array(gray_zoomed)
        zoomed_array = np.expand_dims(zoomed_array, axis=-1)
        print(f"New shape after slicing: {zoomed_array.shape}\
or {zoomed_img.size}")
        print(zoomed_array)
        plt.imshow(zoomed_array, cmap='gray')
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
