from typing import Sequence

import pytest
from ..hw.Task_1.hw_1_task_2 import check_fibonacci


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([0, 1, 1, 2], True),
        ([0], False),
        ([1, 1, 2], False),
    ],
)
def test_check_fibonacci(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
