import pytest
from Epam_training_HW.hw.hw_3_task_4 import is_armstrong


@pytest.mark.parametrize(
    ("value"),
    [
        (153),
        (407),
        (5),
    ],
)
def test_value_is_armstrong(value: int):
    assert is_armstrong(value) is True


@pytest.mark.parametrize(
    ("value"),
    [
        (10),
        (320),
        (1630),
    ],
)
def test_value_is_not_armstrong(value: int):
    assert is_armstrong(value) is False
