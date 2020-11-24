from Epam_training_HW.hw.hw_1_task_1 import check_power_of_2

import pytest


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(65536, True), (12, False), (0, False)],
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
