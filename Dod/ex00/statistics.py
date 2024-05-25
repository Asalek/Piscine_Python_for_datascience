def checker(args: any):
    '''Check if all args are numbers'''
    for x in args:
        try:
            fNum = float(x)
        except Exception as e:
            print(e)
            exit(0)
        if not isinstance(fNum, (int, float)):
            print("Error")
            exit(0)


def find_nearest_number(number, number_list):
    '''    loop over the array and find the nearst number to it,
    according to number given in params'''

    nearest = None
    min_difference = float('inf')

    for num in number_list:
        difference = abs(number - num)
        if difference < min_difference:
            min_difference = difference
            nearest = num
    return nearest


def mean(args: any):
    '''Mean is calculated by dividing the sum of the
     data values by the number of data values.'''
    return sum(args) / len(args)


def median(array) -> float:
    '''Median is the middle data value Median = {(n + 1) / 2}th,
    at 50% of the data, where there is an equal probability
    of data values falling below or above it.'''

    sort = sorted(array)
    middle = (len(sort) - 1) // 2
    if len(sort) % 2 == 0:
        return float(mean([sort[middle], sort[middle + 1]]))
    else:
        return float(sort[middle])


def quartile(args: any) -> list[float]:
    '''The lower/first quartile is at 25% of the data,
    or the middle between of the lower half of data.\n
    The upper/third quartile is at 75% of the data,
    or the middle between the upper half of data.'''
    sort = sorted(args)
    ret = [0.00, 0.00]

    midd = (len(sort) + 1) // 2
    lowerHalf = sort[:midd]
    upperHalf = sort[midd:]

    Q1 = median(lowerHalf)
    Q3 = median(upperHalf)
    ret = [float(find_nearest_number(Q1, sort)),
           float(find_nearest_number(Q3, sort))]
    return (ret)


def std(args: any):
    '''Standard deviation is a statistical measure
    that tells us how spread out numbers are in a dataset.
    It shows the variation or dispersion from the average (mean).
    It helps in understanding how consistent or variable the data is.'''
    # www.gstatic.com/education/formulas2/553212783/en/population_standard_deviation.svg
    mean_ret = mean(args)

    return (((sum(pow(x - mean_ret, 2) for x in args)) / len(args)) ** 0.5)


def var(args: any):
    '''The term variance refers to a statistical measurement
    of the spread between numbers in a data set.
    More specifically, variance measures how far each number
    in the set is from the mean (average),
    and thus from every other number in the set.
    Variance is often depicted by this
    symbol: σ2'''
    # www.gstatic.com/education/formulas2/553212783/en/sample_variance.svg
    mean_ret = mean(args)

    return (sum(pow(x - mean_ret, 2) for x in args) / len(args))


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''takes x of args and apply to them
        (mean, median, quartile, std and var)'''
    socratic = ["mean", "median", "quartile", "std", "var"]

    if len(args) == 0 or len(kwargs) == 0:
        return print("ERROR")
    stats = list(kwargs.values())
    if any(value not in socratic for value in stats):
        return
    checker(args)
    for x in stats:
        if x == "mean":
            print(f"mean : {mean(args)}")
        if x == "median":
            print(f"median : {median(args)}")
        if x == "quartile":
            print(f"quartile : {quartile(args)}")
        if x == "std":
            print(f"std : {std(args)}")
        if x == "var":
            print(f"var : {var(args)}")


# def main():
#     ft_statistics(1, 42, 360, 11, 64,
#                   toto="mean", tutu="median", tata="quartile")
#     print("-----")
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
#                   hello="std", world="var")
#     print("-----")
#     ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
#                   ejfhhe="heheh", ejdjdejn="kdekem")
#     print("-----")
#     ft_statistics(toto="mean", tutu="median", tata="quartile")

# if __name__ == "__main__":
#     main()
