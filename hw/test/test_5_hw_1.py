from typing import List

import pytest
from Epam_training_HW.hw.Task_1.hw_1_task_5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("value1", "value2", "expected_result"),
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([7, 4, -15, -4, 9, 2, 6, -1], 5, 9),
    ],
)
def test_find_maximal_subarray_sum(
    value1: List[int], value2: int, expected_result: int
):

    actual_result = find_maximal_subarray_sum(value1, value2)
    assert actual_result == expected_result
