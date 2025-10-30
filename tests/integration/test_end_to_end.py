from textutils import core as c

def test_full_text_processing_pipeline():
    """
    Running a first set of end-to-end tests
    """
    text = "Red red BLUE"
    normalized = c.normalize_whitespace(text)
    counts = c.word_count(normalized)
    result = c.top_n(counts, 2)
    assert result == [("red", 2), ("blue", 1)]


def test_case_and_censor_pipeline():
    """
    Running a second set of end-to-end tests
    """
    text_input = "what a great day! is THIS fun? absolutely."
    text_step_1 = c.capitalize_sentences(text_input)
    text_step_2 = c.alternate_case(text_step_1)
    text_step_3 = c.censor_vowels(text_step_2)
    assert text_step_3 == "Wh*t * gR**t d*y! *s tH*S F*N? *Bs*l*t*lY."