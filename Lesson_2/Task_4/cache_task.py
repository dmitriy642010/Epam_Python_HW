from collections.abc import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    key = []
    value = []

    def wrapper(*args: Any) -> Any:
        if args in key:
            return value[key.index(args)]
        else:
            key.append(args)
            value.append(func(*args))
            return value[-1]

    return wrapper
