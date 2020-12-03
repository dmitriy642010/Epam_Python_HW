import pytest
from Epam_training_HW.hw.Task_3.hw_3_task_2 import helper_calc


@pytest.mark.timeout(60)
def test_fast_calculate():
    assert helper_calc() == 1025932
