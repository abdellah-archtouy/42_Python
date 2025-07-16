import sys
import string


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more argument")
        sys.exit(1)
    try:
        pun = 0
        upper = 0
        lower = 0
        space = 0
        digits = 0
        if len(sys.argv) == 2:
            text = str(sys.argv[1])
        else:
            text = input("What is the text to count? ")

        for char in text:
            if char in string.punctuation:
                pun += 1
            elif char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isspace():
                space += 1
            elif char.isdigit():
                digits += 1

        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letter")
        print(f"{lower} lower letter")
        print(f"{pun} punctuation marks")
        print(f"{space} spaces")
        print(f"{digits} digits")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
