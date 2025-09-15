import sys


def mylen(seq) -> int:
    """count len of a string"""
    count = 0
    for item in seq:
        count += 1
    return count


def clean_arg(s: str) -> str:
    "remove white space between and after a string"
    start: int = 0
    end: int = mylen(s) - 1
    while start <= end and s[start] == " ":
        start += 1
    while end >= start and s[end] == " ":
        end -= 1
    return s[start: end + 1]


def is_valid_integer(s: str) -> bool:
    """true of false if the string is a valid integer"""
    if mylen(s) == 0:
        return False
    if s[0] in ("-", "+"):
        if mylen(s) == 1:
            return False
        s = s[1:]
    for c in s:
        if not ("0" <= c <= "9"):
            return False
    return True


def find_number(c: str) -> int:
    """transform a char number into int number"""
    digits: str = "0123456789"
    i: int = 0
    while i < 10:
        if c == digits[i]:
            return i
        i += 1
    return -1


def my_atoi(s: str) -> int:
    """transform a string of format [- or +123321...] into integer, the string has to be a valid integer"""
    sign: int = 1
    i: int = 0
    if s[0] == "-":
        sign = -1
        i = 1
    elif s[0] == "+":
        i = 1
    num: int = 0
    while i < mylen(s):
        num = num * 10 + find_number(s[i])
        i += 1
    return sign * num


def strToList(s: str, charset: str = " ") -> list:
    """Splits a string into a list of words, using any character in charset as separator."""
    result: list = []
    word: str = ""
    i: int = 0
    while i < mylen(s):
        if s[i] not in charset:
            word += s[i]
        else:
            if mylen(word) > 0:
                result.append(word)
                word = ""
        i += 1
    if mylen(word) > 0:
        result.append(word)
    return result


def ft_filter(function, iterable) -> list:
    """Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return [item for item in iterable if function(item)]


def filterstring(args: str) -> None:
    """Output a list of words from args[1] that have a length greater than args[2]."""
    lst: list = strToList(args[1])
    num: int = my_atoi(args[2])
    lst = ft_filter(lambda args: mylen(args) > num, lst)
    print(lst)
    return


def main() -> None:
    """check if args are valids"""
    args: list[str] = sys.argv
    try:
        assert mylen(args) == 3, "The arguments are bad"
        args[2] = clean_arg(args[2])
        assert is_valid_integer(args[2]), "The arguments are bad"
        filterstring(args)
    except AssertionError as msg:
        print(msg)
    return


if __name__ == "__main__":
    main()
