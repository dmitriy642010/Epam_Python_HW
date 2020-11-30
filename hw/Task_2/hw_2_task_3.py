import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[Any]:
    return list(itertools.product(*args))
