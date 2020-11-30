from ..Task_3.hw_3_task_2 import helper_calc, slow_calculate


def test_fast_calculate():
    res_slow = sum(slow_calculate(i) for i in range(10))
    res_fast = helper_calc()
    assert res_slow == res_fast
