import sys


def mylen(seq):
    """Counts the length of a sequence without using len()."""

    count = 0
    for item in seq:
        count += 1
    return count


def main():
    """Takes a single string argument and displays the sums of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces."""

    args = sys.argv
    argsLen = mylen(args)

    if argsLen < 2:
        line = ""
        for firstLine in sys.stdin:
            line = firstLine
            break
        countULPDS(line)
    elif argsLen > 2:
        print("Error: too much arguments.")
    else:
        countULPDS(args[1])
    return


def countULPDS(line):
    """just counting word and printing"""

    upper = 0
    lower = 0
    punctuation = 0
    digits = 0
    spaces = 0
    punctuationMarks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for c in line:
        if 'A' <= c <= 'Z':
            upper += 1
        elif 'a' <= c <= 'z':
            lower += 1
        elif c in punctuationMarks:
            punctuation += 1
        elif c in " \t\n\r\v\f":
            spaces += 1
        elif '0' <= c <= '9':
            digits += 1
    print(
        f"The text contains {mylen(line)} characters:\n"
        f"{upper} upper letters\n"
        f"{lower} lower letters\n"
        f"{punctuation} punctuation marks\n"
        f"{spaces} spaces\n"
        f"{digits} digits"
    )
    return


if __name__ == "__main__":
    main()
