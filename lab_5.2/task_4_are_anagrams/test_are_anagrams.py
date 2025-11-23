import pytest
from task_4_are_anagrams.are_anagrams import are_anagrams

@pytest.mark.parametrize("w1, w2, expected", [
    ("listen", "silent", True),
    ("Race", "Care", True),
    ("hello", "world", False),
    ("", "", True),
    ("a", "a", True),
    ("abc", "cab", True),
    ("abc", "abcc", False),
    ("Акт", "Тка", True),  # кириллица
])
def test_are_anagrams(w1, w2, expected):
    assert are_anagrams(w1, w2) == expected
