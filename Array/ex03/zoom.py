from load_image import ft_load
from numpy import array, ndarray
from PIL import Image
import matplotlib.pyplot as plt


def main():
    img_array = ft_load("animal.jpeg")
    img = Image.fromarray(img_array, 'RGB')
    
    width, height = img.size
    

if __name__ == "__main__":
    main()