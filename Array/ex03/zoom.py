from load_image import ft_load
from numpy import array, ndarray
import numpy as np
from PIL import Image


def main():
    """
    This function loads an image, zooms in on it by cropping the center,
    and converts the zoomed image to grayscale.
    It then displays the zoomed grayscale image.
    """
    image_array =  ft_load("animal.jpeg")

    image = Image.fromarray(np.uint8(image_array))
    
    zoom_factor = 3
    img_array = np.array(image)
    print(img_array)
    h, w, _ = img_array.shape  
    new_h = 400
    new_w = 400
    # top, left = (h - new_h) // 2, (w - new_w) // 2
    top = 100
    left = 450
    bottom, right = top + new_h, left + new_w
    cropped_array = img_array[top:bottom, left:right]
    zoomed_image = Image.fromarray(cropped_array).resize((w, h), Image.LANCZOS)
    grayscale_array = np.mean(cropped_array, axis=2, keepdims=True).astype(np.uint8)
    print(f"New shape after slicing: {grayscale_array.shape}")
    print(grayscale_array)
    zoomed_image = Image.fromarray(grayscale_array.squeeze())
    zoomed_image.show()    

if __name__ == "__main__":
    main()
