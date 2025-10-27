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



#Test Alessandro