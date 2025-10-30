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
    assert c.remove_punctuation(text) == "Hello world Its a great day"

def test_word_lengths():    
    text = "Hello, world!"
    assert c.word_lengths(text) == [5, 5]
    
def test_strip_accents():
    text = "Café naïve façade"
    assert c.strip_accents(text) == "Cafe naive facade"

def test_slugify():
    text = "Hello World! This is TextUtils."
    assert c.slugify(text) == "hello-world-this-is-textutils"
    
def test_count_vowels():
    text = "Hello World"
    assert c.count_vowels(text) == 3

def test_camel_to_snake(): #note , we assume acronyms (eg HTML) are 4 seperate words. and therefore will be H_T_M_L, not HTML.
    assert c.camel_to_snake("CamelCase") == "camel_case"
    assert c.camel_to_snake("SimpleTest") == "simple_test"
    assert c.camel_to_snake("thisIsCamelCase") == "this_is_camel_case"

def test_truncate():
    assert c.truncate("Hello World", 5) == "He..."
    assert c.truncate("Hello", 10) == "Hello"
    assert c.truncate("", 5) == ""
    
def test_collapse_duplicates():
    assert c.collapse_duplicates("bookkeeper", "o") == "bokkeeper"
    assert c.collapse_duplicates("a b a", "a") == "a b a"
    assert c.collapse_duplicates("", "a") == ""

def test_is_anagram():
        assert c.is_anagram("listen", "silent") == True
        assert c.is_anagram("LiStEn", "sIlEnT") == True
        assert c.is_anagram("listen", "listen") == True
        assert c.is_anagram("listen", "listenl") == False
        assert c.is_anagram("", "") == True

def test_replace_numbers():
    assert c.replace_numbers("I have 2 dogs and 1 cat") == "I have two dogs and one cat"
    assert c.replace_numbers("2025") == "twozerotwofive"
    assert c.replace_numbers("no digits") == "no digits"

def test_sentence_count():
    assert c.sentence_count("Hi. How are you? Fine!") == 3
    assert c.sentence_count("No punctuation here") == 0

def test_average_word_length():
    assert c.average_word_length("") == 0
    assert c.average_word_length("Hi!") == 2

def test_compare_texts():
    assert c.compare_texts("I love data", "I love data") == 1.0
    assert c.compare_texts("apple", "banana") == 0.0
    assert c.compare_texts("Data Science", "data science") == 1.0

def test_is_palindrome():
    assert c.is_palindrome('bro') == False
    assert c.is_palindrome('oro') == True

def test_reverse_words():
    assert c.reverse_words('two words') == 'Insert a single word'
    assert c.reverse_words('Word') == 'droW'

def test_capitalize_sentences():
    assert c.capitalize_sentences('hello. does this work? yes.') == 'Hello. Does this work? Yes.'

def test_unique_words():
    assert c.unique_words('Data data') == {'data'}
    assert c.unique_words('I love data') == {'i', 'love', 'data'}


def test_alternate_case_basic():
    assert c.alternate_case("Hello") == "HeLlO"
    assert c.alternate_case("Hello world") == "HeLlO WoRlD"

def test_censor_vowels_basic():
    assert c.censor_vowels("Hello world") == "H*ll* w*rld"