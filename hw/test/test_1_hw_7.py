import pytest
from Epam_training_HW.hw.Task_7.hw_7_task_1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    ("value_1", "value_2", "expected_result"),
    [
        (example_tree, "RED", 6),
    ],
)
def test_occurrences(value_1, value_2, expected_result):
    assert find_occurrences(value_1, value_2) == expected_result
