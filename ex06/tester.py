from ft_filter import ft_filter
from ft_filterstring import strToList, mylen, my_atoi, filterstring


def test_strToList_basic():
    assert strToList("a b c") == ["a", "b", "c"]


def test_strToList_charset():
    assert strToList("a,b;c", ",; ") == ["a", "b", "c"]


def test_strToList_empty():
    assert strToList("") == []


def test_strToList_spaces():
    assert strToList("   a   b  c   ") == ["a", "b", "c"]


def test_strToList_multiple_separators():
    assert strToList("a,,b;;c", ",;") == ["a", "b", "c"]


def test_mylen():
    assert mylen("abc") == 3
    assert mylen("") == 0
    assert mylen([1, 2, 3]) == 3


def test_my_atoi():
    assert my_atoi("123") == 123
    assert my_atoi("-42") == -42
    assert my_atoi("+7") == 7
    assert my_atoi("0") == 0


def test_filterstring_basic(capsys):
    filterstring(["prog", "a b c", "1"])
    captured = capsys.readouterr()
    assert "[]" in captured.out


def test_filterstring_num(capsys):
    filterstring(["prog", "apple banana cherry", "5"])
    captured = capsys.readouterr()
    assert "['banana', 'cherry']" in captured.out


def test_filterstring_empty(capsys):
    filterstring(["prog", "", "1"])
    captured = capsys.readouterr()
    assert "[]" in captured.out


def test_filterstring_charset(capsys):
    # Suppose filterstring uses strToList with charset
    filterstring(["prog", "a,b;c", "1"])
    captured = capsys.readouterr()
    # If charset not passed, only one element
    assert "['a,b;c']" in captured.out

# Ajoute d'autres cas limites si besoin


# def test_filerdoc():
#     assert filter.__doc__ == ft_filter.__doc__
print(filter.__doc__)
print(ft_filter.__doc__)
