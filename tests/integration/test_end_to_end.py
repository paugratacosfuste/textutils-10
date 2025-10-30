from textutils import core as c  # Import the core module from the textutils package

def test_full_text_processing_pipeline():
    text = "Red red BLUE"  # Input text for testing
    normalized = c.normalize_whitespace(text)  # Remove extra spaces
    counts = c.word_count(normalized)  # Count occurrences of each word
    result = c.top_n(counts, 2)  # Get the two most frequent words
    assert result == [("red", 2), ("blue", 1)]  # Verify that the output matches the expected result
