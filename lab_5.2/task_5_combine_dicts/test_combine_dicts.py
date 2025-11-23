import pytest
from task_5_combine_dicts.combine_dicts import combine_dicts

@pytest.mark.parametrize("d1, d2, expected", [
    ({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 1, "b": 3, "c": 4}),
    ({}, {"x": 10}, {"x": 10}),
    ({"x": 10}, {}, {"x": 10}),
    ({}, {}, {}),
    ({"a": 1}, {"a": 1}, {"a": 1}),
    ({"a": 1, "b": 2}, {"c": 3}, {"a": 1, "b": 2, "c": 3}),
])
def test_combine_dicts(d1, d2, expected):
    assert combine_dicts(d1, d2) == expected
