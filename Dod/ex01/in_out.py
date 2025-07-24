
def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a function that applies the given function to x."""
    count = [x]

    def inner() -> float:
        """Applies the function to the count and returns the result."""
        count[0] = function(count[0])
        return count[0]
    return inner


my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
