import pytest
from Epam_training_HW.hw.Task_7.hw_7_task_2 import backspace_compare


@pytest.mark.parametrize(
    ("value_1", "value_2", "expected_result"),
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ],
)
def test_backspace(value_1, value_2, expected_result):
    assert backspace_compare(value_1, value_2) == expected_result
