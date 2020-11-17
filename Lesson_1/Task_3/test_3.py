import pytest
from max_min import find_maximum_and_minimum

test_file = "numbers.txt"


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (test_file, (45, 90)),
    ],
)
def test_power_of_2(value: str, expected_result: tuple):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
