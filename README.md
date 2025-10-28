# Python for Data Science Assignment 1, Team 10

<br><br>

# Table of Contents
1. [Overview of the Project](#1.-overview-of-the-project)
2. [Structure of the Repository](#2.-structure-of-the-repository)
3. [Code Execution](#3.-code-execution)
4. [Testing](#4.-testing)

<br><br>

# 1. Overview of the Project

In this repository, Team 10 is going to explore different functions to manipulate text inputs, improve readablity, and clean strings. The functions implemented in this project include:

- word_count
- top_n
- normalize_whitespace
- remove_punctuation
- is_palindrome
- unique_words
- reverse_words
- capitalize_sentences
- word_lengths
- strip_accents
- slugify
- count_vowels
- camel_to_snake
- truncate
- collapse_duplicates
- is_anagram
- compare_texts
- replace_numbers
- sentence_count
- average_word_length
- New functions from us HERE

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
├─ environment.yml
├─ pyproject.toml
└─ README.md
# Ignore the A1 file, it will be the submission file 
</pre>



In the core file, all the functions are stored. In the unit test file, all functions are tested. 

<br><br>

# 3. Code Execution
Before running the script, navigate to the project folder in the command line interface (CLI) and activate the environment. The script has dependencies that need to be installed. 
To install all dependencies with the correct versions in the environment, run in micromamba:<br>

    micromamba create -f environment.yml -y
    micromamba activate textutils

This will install all the necessary dependencies. These can also be found in the requirements.txt file, which indicates the respective versions.

To execute the functions, locate your core file through the terminal:
<pre>
    cd src
</pre>

Then, run your input code and the disired function in the following way in the CLI:
<pre>
    python -c "from textutils import #function_name; print(#function_name('#input'))"
</pre>
For example:
<pre>
    python -c "from textutils import word_count; print(word_count('Hello, hello world!'))"
</pre>


<br><br>

# 4. Testing

This workbook uses unit testing and end-to-end testing to varify the code's reliability. To check if all functions are up to date, locate the main directory textutils-10:

<pre>
    cd -
</pre>



and enter in the CLI:
<pre>
    export PYTHONPATH=src
    pytest -v
</pre>
