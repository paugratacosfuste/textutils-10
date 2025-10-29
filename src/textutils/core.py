'''
This this the core module of the textutils package to do all the functions
'''


def word_count(text):
    """
    Count the occurrences of each word in the given text (case-insensitive).
    """

    text = text.lower()
    text = remove_punctuation(text) # uses function from below since otherwise counts punctuation
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_n(counts, n):
    """
    Return the top-N words by frequency, ties alphabetical.
    """
    def sort_key(item):
        word, count = item
        return (-count, word)  # negative for descending count

    sorted_items = sorted(counts.items(), key=sort_key)
    return sorted_items[:n]

def normalize_whitespace(text):
    """
    Collapse runs of whitespace (spaces, tabs, newlines) into a single space,
    and trim spaces.
    """
    # Split on any whitespace with split() function
    words = text.split()

    # Join them back with a single space with join function
    return " ".join(words)


import string
def remove_punctuation(text):
    """
    Remove all punctuation from the text while keeping spaces and letters.
    """
    result = ""
    for char in text:
        if char not in string.punctuation:
            result += char
    return result

def word_lengths(text):
    """
    Return a list of the lengths of each word in the text.
    """
    text = remove_punctuation(text) # uses function from above since otherwise counts punctuation
    words = text.split()
    lengths = [len(word) for word in words]
    return lengths

def strip_accents(text):
    """
    Remove accents from characters in the text.
    """
    import unicodedata
    normalized = unicodedata.normalize('NFD', text)
    stripped = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
    return stripped

def slugify(text):
    """
    Convert text to a URL-friendly slug.
    """
    text = text.lower()
    text = strip_accents(text)  # uses function from above
    text = remove_punctuation(text)  # uses function from above
    text = normalize_whitespace(text)  # uses function from above
    slug = text.replace(" ", "-")
    return slug

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count

def replace_numbers(text):
    numbers = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
    }
    result = ""
    for ch in text:
        if ch in numbers:
            result += numbers[ch]
        else:
            result += ch
    return result

def sentence_count(text):
    count = 0
    for ch in text:
        if ch in [".", "!", "?"]:
            count += 1
    return count

def average_word_length(text):
    words = text.split()
    if not words:
        return 0
    total_length = 0
    for word in words:
        clean = word.strip(".,!?;:")
        total_length += len(clean)
    return total_length / len(words)

def is_palindrome(text):
    if ' ' in text:
        return 'Insert a single word'
    else:
        word = []
        for x in text:
            word.insert(0, x)
        reversed_word = ''.join(word)
        if reversed_word == text:
            return True
        else:
            return False