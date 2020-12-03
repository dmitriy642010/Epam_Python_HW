from functools import wraps
from typing import Callable


def decorator(func: Callable) -> Callable:
    @wraps(func)
    def new_wrapper(wrapper: Callable) -> Callable:
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__original_func = func
        return wrapper

    return new_wrapper


def print_result(func: Callable) -> Callable:
    @decorator(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function."""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper
