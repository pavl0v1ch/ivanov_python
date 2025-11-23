import pytest
from task_3_is_palindrome.is_palindrome import is_palindrome

@pytest.mark.parametrize("input_value, expected", [
    ("level", True),
    ("RaceCar", True),
    ("hello", False),
    ("", True),               # пустая строка — технически палиндром
    ("а роза упала на лапу азора", False),  # пробелы не игнорируются
    (12321, True),
    (12345, False),
    (1, True),
])
def test_is_palindrome(input_value, expected):
    assert is_palindrome(input_value) == expected
