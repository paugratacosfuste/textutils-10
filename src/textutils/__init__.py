from .core import (
    word_count,
    top_n,
    normalize_whitespace,
    remove_punctuation,
    #is_palindrome, #A
    #unique_words, #A
    #reverse_words, #A
    #capitalize_sentences,#A
    word_lengths, #L
    strip_accents, #L
    slugify, #L
    count_vowels, #L
    #camel_to_snake,#S
    #truncate, #S
    #collapse_duplicates, #S
    #is_anagram, #S
    #compare_texts, #s
    replace_numbers, #P
    sentence_count, #p
    average_word_length, #P
)

# Define __all__ for clarity
__all__ = [
    "word_count",
    "top_n",
    "normalize_whitespace",
    "remove_punctuation",
    "is_palindrome",
    "unique_words",
    "reverse_words",
    "capitalize_sentences",
    "word_lengths",
    "strip_accents",
    "slugify",
    "count_vowels",
    "camel_to_snake",
    "truncate",
    "collapse_duplicates",
    "is_anagram",
    "compare_texts",
    "replace_numbers",
    "sentence_count",
    "average_word_length",
]
