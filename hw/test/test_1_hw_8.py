import os

from Epam_training_HW.hw.Task_8.hw_8_task_1 import KeyValueStorage

import pytest


@pytest.fixture()
def filename():
    filename = "test_task_1_hw_8.txt"
    with open(filename, "w"):
        pass
    yield filename
    os.remove(filename)


def fill_the_file(dict_to_write, filename):
    with open(filename, "a") as file:
        for key, value in dict_to_write.items():
            file.write(f"{key}={value}\n")


def test_key_value_storage(filename):
    dict_to_test = {"name": "kek", "power": 9001}
    fill_the_file(dict_to_test, filename)
    storage = KeyValueStorage(filename)
    for key in dict_to_test:
        assert storage[key] == dict_to_test[key]
