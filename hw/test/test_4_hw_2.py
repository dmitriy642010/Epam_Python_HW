from typing import List

from Epam_training_HW.hw.Task_2.hw_2_task_4 import cache


def func(a, b):
    return (a ** b) ** 2


def test_cache():
    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def foo(nums: List[int]) -> List[int]:
    return [x // 2 for x in nums]


def test_cache_list_args():
    cache_func = cache(foo)
    some = [1, 2, 3, 4, 5, 6]
    val_1 = cache_func(some)
    val_2 = cache_func(some)
    assert val_1 is val_2


def fun(*, param=10):
    return param


def test_cache_2():
    cache_func = cache(fun)
    some = 100, 200
    val_1 = cache_func(some)
    val_2 = cache_func(some)
    assert val_1 is val_2
