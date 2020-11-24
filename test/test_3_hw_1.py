import os
import pytest
from Epam_training_HW.hw.hw_1_task_3 import find_maximum_and_minimum


@pytest.fixture()
def file_name():
    file = "numbers.txt"
    with open(file, "w") as f:
        f.write("45 \n 78 \n 90 \n 87 \n")

    yield file
    os.remove(file)


def test_power_of_2(file_name):
    actual_result = find_maximum_and_minimum("numbers.txt")

    assert actual_result == (45, 90)
