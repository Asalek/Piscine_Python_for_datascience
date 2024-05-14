import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array
    based on the provided start and end arguments.
    """
    old_len = len(family[0])
    newArray = np.array(family)
    for x in newArray:
        if (old_len != len(x)):
            print("List Provided must contains lists with the same length")
            return []

    sliced_list = slice(start, end)
    # sliced_list = x[start:end]
    print("My shape is     : ", newArray.shape)
    print("My new shape is : ", newArray[sliced_list].shape)
    return newArray[sliced_list]
