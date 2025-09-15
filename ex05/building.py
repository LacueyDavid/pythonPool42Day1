import sys


def mylen(seq: str) -> int:
    """Counts the length of a sequence without using len()."""

    count: int = 0
    for item in seq:
        count += 1
    return count


def getFirstStdinLine() -> str:
    """Get the first line in stdin"""
    line: str = ""
    while mylen(line) == 0:
        try:
            print("Please provide a string:")
            for firstLine in sys.stdin:
                line = firstLine
                break
        except KeyboardInterrupt:
            print("\nInput cancelled by user (Ctrl+C). Exiting.")
            sys.exit(0)
    return line


def countULPDS(line: str) -> None:
    """(ULPDS stand for upper lower punctuation digit spaces) Takes a single string argument and displays the sums of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces."""

    upper: int = 0
    lower: int = 0
    punctuation: int = 0
    digits: int = 0
    spaces: int = 0
    punctuationMarks: str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

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


def main() -> None:
    """check if args are valid and then pass the string to countULPDS"""
    args: list[str] = sys.argv
    argsLen: int = mylen(args)

    try:
        assert argsLen <= 2, "more than one argument is provided"
        if argsLen < 2:
            line: str = getFirstStdinLine()
            countULPDS(line)
        elif argsLen == 2:
            countULPDS(args[1])
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        sys.exit(1)
    return


if __name__ == "__main__":
    main()
