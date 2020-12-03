from typing import List

import pytest
from ..hw.Task_1.hw_1_task_4 import check_sum_of_four


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected_result"),
    [
        ([], [], [], [], 0),
        ([0, -5, 2, 7], [0, 5, -2, 7], [0, 5, 2, -7], [0, 5, 2, 7], 6),
        ([-1], [0], [0], [1], 1),
        ([0], [0], [0], [0], 1),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):

    actual_result = check_sum_of_four(a, b, c, d)
    assert actual_result == expected_result
