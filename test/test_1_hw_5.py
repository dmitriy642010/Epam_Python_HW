from datetime import timedelta

from ..hw.Task_5.hw_5_task_1 import Homework, Student, Teacher

import pytest


@pytest.fixture()
def student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def teacher():
    return Teacher("Daniil", "Shadrin")
