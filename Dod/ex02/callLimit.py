def callLimit(limit: int):
    count = [0]

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            if count[0] < limit:
                count[0] += 1
                return function(*args, **kwds)
            else:
                err_msg = \
                    f"function {function.__name__} at {hex(id(function))}"
                print(f"Error: <{err_msg}> call too many times")
                return None
        return limit_function
    return callLimiter
