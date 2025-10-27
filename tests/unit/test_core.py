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
    
def test_replace_numbers():
    assert replace_numbers("I have 2 dogs and 1 cat") == "I have two dogs and one cat"
    assert replace_numbers("2025") == "twozerotwofive"
    assert replace_numbers("no digits") == "no digits"
    print("replace_numbers passed")

def test_sentence_count():
    assert sentence_count("Hi. How are you? Fine!") == 3
    assert sentence_count("No punctuation here") == 0
    assert sentence_count("One... two.") == 2
    print("sentence_count passed")

def test_average_word_length():
    assert round(average_word_length("I love AI"), 2) == 2.33
    assert average_word_length("") == 0
    assert average_word_length("Hi!") == 2
    assert round(average_word_length("A cat, a dog."), 2) == 2.25
    print("average_word_length passed")



