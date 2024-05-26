def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if count > limit:
                print(f'Error: {function} call too many times')
                return None
            return function(*args, **kwds)
        return limit_function
    return callLimiter