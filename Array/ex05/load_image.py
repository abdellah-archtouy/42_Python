from numpy import array
from PIL import Image


def ft_load(path: str) -> array:
    """
    Load an image from the specified path and convert it to a 3D numpy array.
    :param path: Path to the image file.
    :return: 3D numpy array representing the image.
    """
    try:
        assert isinstance(path, str), \
            "AssertionError: Input must be a string."
        assert path.endswith(('.jpg', '.jpeg', '.png')), \
            "AssertionError: Input must be a valid image \
file (.jpg, .jpeg, .png)."
        img = Image.open(path)
        img = img.convert("RGB")
        arr = array(img)
        assert arr.ndim == 3, \
            "AssertionError: The array must be 3-dimensional."
        assert arr.shape[2] == 3, \
            "AssertionError: The array must have 3 channels (RGB)."
        print(f"The shape of image is: {arr.shape}")
        print(arr[:1])
        img.show()
        return arr
    except AssertionError as e:
        print(e)
