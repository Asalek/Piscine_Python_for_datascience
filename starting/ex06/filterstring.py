import sys
from ft_filter import ft_filter


def main():
    """
        accepts two arguments: a string(S), and an integer(N).
        output:  a list of words from S that have a length greater than N.
    """
    if len(sys.argv) != 3:
        print("Usage: EXpected input : <string> <int>")
        sys.exit(1)
    text = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the second argument is not an integer")
        sys.exit(1)
    if not isinstance(text, str) or not isinstance(n, int):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    filter_ret = ft_filter(lambda x: len(x) > n, text.split())
    print(list(filter_ret))


main()
