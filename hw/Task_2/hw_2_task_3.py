import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    return list(itertools.product(*args))
