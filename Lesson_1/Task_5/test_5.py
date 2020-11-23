from typing import List

import pytest
from sub_array import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("value1", "value2", "expected_result"),
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([7, 4, -15, -4, 9, 2, 6, -1], 5, 9),
    ],
)
def test_find_maximal_subarray_sum(s: List[int], k: int, expected_result: int):

    actual_result = find_maximal_subarray_sum(s, k)
    assert actual_result == expected_result
