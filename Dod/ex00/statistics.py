
def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Function to compute statistics on a list of numbers.
    It accepts a variable number of positional arguments (numbers)
    and keyword arguments to specify the type of statistics to compute.
    Keyword arguments can include:
        - 'mean', 'median', 'quartile' for basic statistics
        - 'std', 'var' for standard deviation and variance
    """
    try:
        # assert len(args) > 0, "At least one argument is required"
        # assert len(kwargs) > 1, "At least two keyword arguments are required"
        assert all(isinstance(arg, (int, float)) for arg in args), \
            "All arguments must be numbers"
        assert all(isinstance(value, str) for value in kwargs.values()), \
            "All keyword arguments must be strings"
        allowed = [["mean", "median", "quartile"], ["std", "var"]]
        check1 = all(value in allowed[0] for value in kwargs.values())
        check2 = all(value in allowed[1] for value in kwargs.values())
        if check1 and len(kwargs) == 3:
            if len(args) == 0:
                print("ERROR")
                print("ERROR")
                print("ERROR")
                return
            data = sorted(args)
            n = len(data)
            mean = sum(data) / n
            if n % 2 == 0:
                median = (data[n//2 - 1] + data[n // 2]) / 2
            else:
                median = data[n // 2]
            quartile1 = float(data[n // 4] if n >= 4 else None)
            quartile2 = float(data[n * 3 // 4] if n >= 4 else None)
            print(f"mean: {mean}")
            print(f"median: {median}")
            print(f"quartile: {[quartile1, quartile2]}")
        elif len(kwargs) == 2 and check2:
            if len(args) == 0:
                print("ERROR")
                print("ERROR")
                return
            mean = sum(args) / len(args)
            variance = sum((x - mean) ** 2 for x in args) / len(args)
            std_dev = variance ** 0.5
            print(f"std: {std_dev}")
            print(f"var: {variance}")
        else:
            return
    except Exception as e:
        print(f"Error: {e}")
