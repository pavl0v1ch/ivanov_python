import pytest
from task_2_unique_elements.find_unique import find_unique

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 2, 3, 4, 4, 5], [1, 3, 5]),
    (["a", "b", "a", "c"], ["b", "c"]),
    ([1, 1, 1, 1], []),
    ([], []),
    ([10], [10]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
])
def test_find_unique(input_list, expected):
    assert find_unique(input_list) == expected
