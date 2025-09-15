from building import main, countULPDS, mylen, getFirstStdinLine


def test_countULPDS_empty(capsys):
    countULPDS("")
    captured = capsys.readouterr()
    assert "The text contains 0 characters" in captured.out


def test_countULPDS_full(capsys):
    text = (
        "Python 3.0, released in 2008, was a major revision that is not completely "
        "backward-compatible with earlier versions. Python 2 was discontinued with "
        "version 2.7.18 in 2020."
    )
    countULPDS(text)
    captured = capsys.readouterr()
    expected = (
        "The text contains 171 characters:\n"
        "2 upper letters\n"
        "121 lower letters\n"
        "8 punctuation marks\n"
        "25 spaces\n"
        "15 digits"
    )
    assert expected in captured.out


def test_main_doc():
    main_doc = """check if args are valid and then pass the string to countULPDS"""
    assert main.__doc__ == main_doc


def test_countULPDS_doc():
    countULPDS_doc = """(ULPDS stand for upper lower punctuation digit spaces) Takes a single string argument and displays the sums of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces."""
    assert countULPDS.__doc__ == countULPDS_doc


def test_mylen_doc():
    mylen_doc = """Counts the length of a sequence without using len()."""
    assert mylen.__doc__ == mylen_doc


def test_getFirstStdinLine_doc():
    getFirstStdinLine_doc = """Get the first line in stdin"""
    assert getFirstStdinLine.__doc__ == getFirstStdinLine_doc
