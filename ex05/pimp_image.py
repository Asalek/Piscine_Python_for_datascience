import array
from matplotlib import pyplot as plt
import numpy as np


def ft_invert(array) -> array:
    """
        Inverts the color of the image received.
    """
    # methode_1
    # invTransform = (lambda x: 255 - x)
    # invert = invTransform(array)
    # methode_2
    invert = [[255-v for v in r] for r in array]
    plt.imshow(invert)
    plt.axis('off')
    plt.show()
    return invert


def ft_red(array) -> array:
    """
        gradiant the color of the image received to red.
    """
    red = np.copy(array)
    for i in range(len(red)):
        for j in range(len(red[i])):
            red[i][j][1] = 0
            red[i][j][2] = 0
    plt.imshow(red)
    plt.axis('off')
    plt.show()
    return red


def ft_green(array) -> array:
    """
        gradiant the color of the image received to green.
    """
    green = np.copy(array)
    for i in range(len(green)):
        for j in range(len(green[i])):
            green[i][j][0] = 0
            green[i][j][2] = 0
    plt.imshow(green)
    plt.axis('off')
    plt.show()
    return green


def ft_blue(array) -> array:
    """
        gradiant the color of the image received to blue.
    """
    blue = np.copy(array)
    for i in range(len(blue)):
        for j in range(len(blue[i])):
            blue[i][j][0] = 0
            blue[i][j][1] = 0
    plt.imshow(blue)
    plt.axis('off')
    plt.show()
    return blue


def ft_grey(array) -> array:
    """
        gradiant the color of the image received to blue.
    """
    grey = np.copy(array)
    for i in range(len(grey)):
        for j in range(len(grey[i])):
            r = grey[i][j][0] * 0.299
            g = grey[i][j][1] * 0.587
            b = grey[i][j][2] * 0.114
            grey[i][j][0] = r + g + b  # R
            grey[i][j][1] = r + g + b  # G
            grey[i][j][2] = r + g + b  # B
    plt.imshow(grey)
    plt.axis('off')
    plt.show()
    return grey
