import sys

def is_odd(number: int) -> bool:
    return number % 2 != 0

def main():
    if len(sys.argv) < 2:
        sys.exit(0)
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        if is_odd(number):
            print("I'm Odd")
        else:
            print("I'm Even")
    except ValueError:
        print("AssertionError:  argument is not an integer")
        sys.exit(1)
    sys.exit(0)

main()

