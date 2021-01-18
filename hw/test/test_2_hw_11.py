from Epam_training_HW.hw.Task_11.hw_11_task_2 import (
    ElderDiscount,
    MorningDiscount,
    Order,
)


def test_order():
    order_1 = Order(100, MorningDiscount)
    assert order_1.final_price() == 75

    order_2 = Order(100, ElderDiscount)
    assert order_2.final_price() == 85
