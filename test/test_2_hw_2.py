from typing import List, Tuple

import pytest
from ..hw.Task_2.hw_2_task_2 import major_and_minor_elem


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([3, 2, 3], (3, 2)),
        ([7, 8, 7, 8, 7, 7, 5], (7, 5)),
    ],
)
def test_major_and_minor_elem(value: List, expected_result: Tuple[int, int]):
    actual_result = major_and_minor_elem(value)

    assert actual_result == expected_result
