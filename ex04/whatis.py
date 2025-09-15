import sys


def mylen(seq):
    count = 0
    for item in seq:
        count += 1
    return count


def clean_arg(s):
    start = 0
    end = mylen(s) - 1
    while start <= end and s[start] == " ":
        start += 1
    while end >= start and s[end] == " ":
        end -= 1
    return s[start: end + 1]


def is_valid_integer(s):
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


def find_number(c):
    digits = "0123456789"
    i = 0
    while i < 10:
        if c == digits[i]:
            return i
        i += 1
    return -1


def my_atoi(s):
    sign = 1
    i = 0
    if s[0] == "-":
        sign = -1
        i = 1
    elif s[0] == "+":
        i = 1
    num = 0
    while i < mylen(s):
        num = num * 10 + find_number(s[i])
        i += 1
    return sign * num


def main():
    seq: list[str] = sys.argv
    len: int = mylen(seq)
    if len == 1:
        return
    try:
        assert len <= 2, "AssertionError: more than one argument is provided"
        arg = clean_arg(seq[1])
        assert is_valid_integer(
            arg), "AssertionError: argument is not an integer"
        result = my_atoi(arg)
        if result % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as msg:
        print(msg)


main()
