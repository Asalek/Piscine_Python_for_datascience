import numpy as np
import array
import matplotlib.pyplot as plt
from load_image import ft_load


def trim(array, x, y, width, height, depth=3):
    """
    Trim an array using the given parameters
    """
    return array[y:y+width, x:x+height, :depth]


def zoom_in(img: array):
    image = trim(img, 400, 90, 400, 400, 1)
    print(f'New shape after slicing: {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)
    # Display the image In pyplot App
    image = np.squeeze(image)
    plt.imshow(image, cmap='gray')
    # plt.axis('off')
    plt.show()


def main():
    """
        Zoom In and show X,Y of the zoomed Image
    """
    data = []
    try:
        data = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        exit()
    if (len(data)):
        zoom_in(data)


if __name__ == '__main__':
    main()
