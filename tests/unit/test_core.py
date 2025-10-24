'''
For testing the core module
'''

from textutils import word_count
def test_word_count_basic():
    text = "Hello, hello world!"
    result = word_count(text)
    assert result == {"hello": 2, "world": 1}



from textutils import top_n
def test_top_n_tiebreaker():
    counts = {"hello": 3, "apple": 3, "world": 1}
    result = top_n(counts, 2)
    assert result == [("apple", 3), ("hello", 3)]



from textutils import normalize_whitespace
def test_normalize_whitespace_basic():
    text = "  Hello   world!   \nThis   is   text. "
    assert normalize_whitespace(text) == "Hello world! This is text."



from textutils import remove_punctuation
def test_remove_punctuation():
    text = "Hello, world! It's a great day."
    assert remove_punctuation(text) == "Hello world Its a great day"