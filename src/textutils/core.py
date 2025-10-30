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

def camel_to_snake(text):

    result = "" #store an empty string
    for i, char in enumerate(text): 
        if char.isupper() and i != 0: #goes through the whole word, find if any char is capital besides [0]
            result += "_"  # if it is, adds underscore before the letter
        result += char.lower()  # finally, ends by adding back the lowercase into result
    return result

def truncate(text, n): #takes a text, and a max 'n-length' that you desire, chopping text if too long

    if len(text) > n:
        return text[:n-3] + "..." #the -3 is because the '...' stands in place of the last three letters 
    return text

def collapse_duplicates(text, char): #takes a text, and char that we don't want run-on duplicates for

    result = "" #store empty string, which we'll add into
    for i in range(len(text)): #reads through each letter in text

        if i == 0 or text[i] != char or text[i-1] != char: #all three conditions MUST be false for the word to not be added
            result += text[i] 
    return result

def is_anagram(a, b):

    a = a.lower().replace(" ", "") #make all of a + b lowercase, removing spaces as well
    b = b.lower().replace(" ", "")
    
    return sorted(a) == sorted(b) #sorted seperates into individual characters alphabetically. if anogram, it will be TRUE
#SEAN AREA END

def replace_numbers(text): #replacing each number for its written counter part
    numbers = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
    } # definition through a library of each counterparts
    result = ""
    for ch in text:
        if ch in numbers:
            result += numbers[ch]
        else:
            result += ch
    return result # loop that looks for the counterpart of the input

def sentence_count(text): #functions that counts the amount of sentences in a text
    count = 0 #counter set to 0
    for ch in text: 
        if ch in [".", "!", "?"]:
            count += 1
    return count #loop that uses punctuation signs to find the end of a sentences and add 1 to counter

def average_word_length(text): #function that counts the average word length in a given text
    words = text.split() #splitting the woprds of the text
    if not words:
        return 0 #making sure the text has words that we can count
    total_length = 0 
    for word in words:
        clean = word.strip(".,!?;:")
        total_length += len(clean) # loop that counts the splitted words and adds the amount to the counter
    return total_length / len(words) #returning total length

def reverse_words(text): #function that returns the word reversed
    if ' ' in text:
        return 'Insert a single word' #making sure only one word is provided
    else:
        word = [] 
        for x in text:
            word.insert(0, x)
        reversed_word = ''.join(word) #loop to reverse the word
        return reversed_word

def is_palindrome(text): 
    if ' ' in text:  # Check if input contains spaces
        return 'Insert a single word'
    else:
        word = []  # Initialize empty list to store reversed characters
        for x in text:  # Loop through each character in the text
            word.insert(0, x)  # Insert character at the start of the list (reverses order)
        reversed_word = ''.join(word)  # Join list into a string
        if reversed_word == text:  # Compare reversed word with original
            return True
        else:
            return False

def unique_words(text):
    text = text.lower()  # Convert text to lowercase for consistency
    word_list = text.split()  # Split text into a list of words
    word_unique = set()  # Initialize an empty set to store unique words
    for word in word_list:  # Loop through each word in the list
        word_unique.add(word)  # Add word to the set (duplicates ignored)
    return word_unique  # Return the set of unique words

def capitalize_sentences(text):
    result = ''  # Store the final formatted text
    capitalize_next = True  # Flag to indicate when to capitalize
    for ch in text:  # Loop through each character in the text
        if capitalize_next and ch.isalpha():  # If flag is True and char is a letter
            result += ch.upper()  # Capitalize the character
            capitalize_next = False  # Reset flag until next sentence
        else:
            result += ch  # Add character as is
        if ch in '.!?':  # After sentence-ending punctuation
            capitalize_next = True  # Next letter should be capitalized
    return result  # Return the capitalized text

def alternate_case(text):
    return ''.join(
        c.upper() if i % 2 == 0 else c.lower()
        for i, c in enumerate(text)
    )

def censor_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join('*' if c in vowels else c for c in text)