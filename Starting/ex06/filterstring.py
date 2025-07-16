
from ft_filter import ft_filter
import sys


def my_len(string: str, size: int) -> bool:
    if len(string) > size:
        return True
    return False


def main():
    try:
        if len(sys.argv) != 3:
            raise "bad  argument"
        text = str(sys.argv[1]).split()
        size = int(sys.argv[2])
        # print(text)
        # print(size)
        last_list = ft_filter(lambda word: my_len(word, size), text)
        print(list(last_list))
    except Exception as e:
        e = str(e)
        print("AssertionError: the argument are bad ")


if __name__ == "__main__":
    main()
