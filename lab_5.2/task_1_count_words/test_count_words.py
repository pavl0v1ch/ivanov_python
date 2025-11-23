import pytest
from task_1_count_words.count_words import count_words

@pytest.mark.parametrize("sentence, expected", [
    ("Hello world", 2),
    ("Python is powerful", 3),
    ("   spaced   out   words   ", 3),
    ("", 0),
    ("     ", 0),
    ("One", 1),
    ("line\nbreaks are words too", 5),
    ("\n\nmultiple\n\nbreaks", 2),
])
def test_count_words(sentence, expected):
    assert count_words(sentence) == expected
