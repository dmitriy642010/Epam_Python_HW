from typing import Any, List

from combinations import combi

import pytest


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([[1, 2], [3, 4]], [(1, 3), (1, 4), (2, 3), (2, 4)]),
        ([["a", "b"], ["c", "d"]], [('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]),
    ],
)
def test_combinations(value: List[Any], expected_result: List[List]):
    actual_result = combi(*value)

    assert actual_result == expected_result
