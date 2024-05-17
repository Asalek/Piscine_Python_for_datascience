# https://docs.python.org/3/library/functions.html#filter
def ft_filter(func, iter):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''

    if (func):
        return (item for item in iter if func(item))
    return (item for item in iter if item)
