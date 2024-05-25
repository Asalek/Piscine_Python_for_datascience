def square(x: int | float) -> int | float:
    '''Return Square of given number X^2'''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''Return Exponentiation of given number X^X'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''Apply function on the given number'''
    # outer.oldX = getattr(outer, "oldX", x)
    def inner() -> float:
        nonlocal x
        x = function(x)
        return x
    return inner


# def main():

#     my_counter = outer(3, square)
#     print(my_counter())
#     print(my_counter())
#     print(my_counter())
#     print("---")
#     another_counter = outer(1.5, pow)
#     print(another_counter())
#     print(another_counter())
#     print(another_counter())


# if __name__ == "__main__":
#     main()
