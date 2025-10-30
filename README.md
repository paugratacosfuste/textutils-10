# Python for Data Science Assignment 1, Team 10
### Members of Team 10:<br>
Sean Amir Hoet<br>
Alessandro Mezzanotte<br>
Pau Gratacos Fuste<br>
Lara Lal Isikci<br>
Jan Erik Sternberg<br>

<br><br>

# Table of Contents
1. [Overview of the Project](#overview-of-the-project)
2. [Structure of the Repository](#structure-of-the-repository)
3. [Code Execution](#code-execution)
4. [Testing](#testing)

<br><br>

# 1. Overview of the Project

In this repository, Team 10 is going to explore different functions to manipulate text inputs, improve readablity, and clean strings. The functions implemented in this project include:

* word_count(text) — case-insensitive counts.  
* top_n(counts, n) — top-N by frequency, ties alphabetical.  
* normalize_whitespace(text) — collapse runs of whitespace, trim ends.  
* remove_punctuation(text) — strip punctuation while keeping spaces and letters.  
* is_palindrome(text) — check if text reads the same backwards (ignore case and spaces).  
* unique_words(text) — return a sorted list of distinct words (case-insensitive).  
* reverse_words(text) — reverse the order of words, not characters.  
* capitalize_sentences(text) — ensure each sentence starts with a capital letter.  
* word_lengths(text) — return a dict mapping words to their lengths.  
* strip_accents(text) — remove accents from characters (e.g., café → cafe).  
* slugify(text) — convert text to lowercase, hyphen-separated safe string.  
* count_vowels(text) — count vowels in the given text.  
* camel_to_snake(text) — convert CamelCase identifiers to snake_case.  
* truncate(text, n) — shorten text to n characters, adding “...” if needed.  
* collapse_duplicates(text, char) — replace runs of the same char with one.  
* is_anagram(a, b) — check if two texts are anagrams (ignore case and spaces).  
* compare_texts(text1, text2) — compute similarity based on common word ratio.  
* replace_numbers(text) — replace digits with their word equivalents (2 → two).  
* sentence_count(text) — count number of sentences in text.  
* average_word_length(text) — compute mean length of words in text.
* alternate_case — capitalize every second letter.
* censor_vowels — censors all the vowels.

<br><br>

# 2. Structure of the Repository
The repository has the following structure:<br>

<pre>
textutils/
├─ src/
│  └─ textutils/
│     ├─ __init__.py
│     └─ core.py
├─ tests/
│  ├─ unit/
│  │  └─ test_core.py
│  └─ integration/
│     └─ test_end_to_end.py
├─ .gitignore
├─ A1.ipynb #it will be the submission file 
├─ environment.yml
├─ pyproject.toml
├─ README.md
└─ setup.cfg
</pre>



In the core file, all the functions are stored. In the unit test file, all functions are tested. 

<br><br>

# 3. Code Execution
Before running the script, navigate to the project folder in the command line interface (CLI) and activate the environment. The script has dependencies that need to be installed. 
To install all dependencies with the correct versions in the environment, run in micromamba:<br>

    micromamba create -f environment.yml -y
    micromamba activate textutils
    pip install -e .

This will install all the necessary dependencies. These can also be found in the requirements.txt file, which indicates the respective versions.

Then, run your input code and the desired function in the following way in the CLI:
<pre>
    python -c "from textutils import #function_name; print(#function_name('#input'))"
</pre>
For example:
<pre>
    python -c "from textutils import word_count; print(word_count('Hello, hello world!'))"
</pre>


<br><br>

# 4. Testing

This workbook uses unit testing and end-to-end testing to verify the code's reliability. To check if all functions are up to date, enter in the CLI:
<pre>
    pytest
</pre>
