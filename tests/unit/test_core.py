'''
For testing the core module
'''
import textutils. core as c

def test_word_count_basic():
    text = "Hello, hello world!"
    assert c.word_count(text) == {"hello": 2, "world": 1}


def test_top_n_tiebreaker():
    counts = {"hello": 3, "apple": 3, "world": 1}
    assert c.top_n(counts, 2) == [("apple", 3), ("hello", 3)]

def test_normalize_whitespace_basic():
    text = "  Hello   world!   \nThis   is   text. "
    assert c.normalize_whitespace(text) == "Hello world! This is text."

def test_remove_punctuation():
    text = "Hello, world! It's a great day."
    assert remove_punctuation(text) == "Hello world Its a great day"


from textutils import word_lengths 
def test_word_lengths():    
    text = "Hello, world!"
    assert word_lengths(text) == [5, 5]
    


from textutils import strip_accents
def test_strip_accents():
    text = "Café naïve façade"
    assert strip_accents(text) == "Cafe naive facade"
    


from textutils import slugify
def test_slugify():
    text = "Hello World! This is TextUtils."
    assert slugify(text) == "hello-world-this-is-textutils"
    

from textutils import count_vowels
def test_count_vowels():
    text = "Hello World"
    assert count_vowels(text) == 3
    




