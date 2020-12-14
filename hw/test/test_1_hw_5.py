import copy
import datetime
import pytest

from Epam_training_HW.hw.Task_5.hw_5_task_1 import Teacher, Student


@pytest.fixture
def teacher():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture
def student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def expired_homework(teacher):
    return teacher.create_homework("Learn functions", 0)


def test_create_teacher(teacher):
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_create_student(student):
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_homework_is_created(teacher):
    homework = teacher.create_homework("Learn functions", 1)
    assert homework.text == "Learn functions"
    assert homework.is_active() is True


def test_homework_deadline():
    homework = Teacher.create_homework("task", 5)
    assert homework.deadline == datetime.timedelta(5)


def test_student_do_homework_in_time(student):
    homework = Teacher.create_homework("Learn functions", 1)
    assert student.do_homework(homework) is homework

    hw_copy = copy.copy(homework)
    assert hw_copy.text == homework.text
    assert hw_copy.deadline == homework.deadline
    assert hw_copy.created == homework.created


def test_do_expired_homework(student, expired_homework, capsys):
    assert student.do_homework(expired_homework) is None
    out, err = capsys.readouterr()
    assert out == "You are late\n"
