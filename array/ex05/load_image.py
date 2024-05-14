import numpy as np
import array
from PIL import Image
import PIL as PIL


def ft_load(path: str) -> array:
    """
    function that loads an image,
    prints its format, and its pixels
    content in RGB format
    """
    numpyImage = np.array([])
    try:
        image = Image.open(path)
        numpyImage = np.asarray(image)
        print("Image Table Shape : ", numpyImage.shape)
        print(f' or ({numpyImage.shape[0]}, {numpyImage.shape[1]})')
        print("Image All Pixels  : \n", numpyImage)
    except FileNotFoundError:
        print("No File with that name found")
    except PIL.UnidentifiedImageError:
        print("If the image cannot be opened and identified.")
    except ValueError:
        print("cann't open the file")
    except TypeError:
        print("formats is not None, a list or a tuple.")
    except Exception:
        print("cann't open the file, check permisions")
    return numpyImage
