import sys
from matplotlib import pyplot as plt
import numpy as np
from load_image import ft_load


def trim(array, x, y, width, height, depth=3):
    """
    Trim an array using the given parameters
    """
    return array[y:y+width, x:x+height, :depth]


def transpose(matrix):
    """
    transpose a matrix (EX: X,Y -> Y,X), works like the original np.transpose()
    """
    matrix2 = np.copy(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            matrix2[i][j] = matrix[j][i]
    return matrix2


def rotate(data):
    """
    rotate an image with -90 degree
    """
    img = trim(data, 450, 100, 400, 400, 1)
    img = transpose(img)
    img = np.squeeze(img)
    print(f"New Shpe after transpose: ({img.shape[0]}, {img.shape[1]})")
    print(img)
    plt.imshow(img, cmap='gray')
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
        sys.exit()
    if (len(data)):
        rotate(data)


if __name__ == '__main__':
    main()
