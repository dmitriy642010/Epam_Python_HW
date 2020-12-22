from Epam_training_HW.hw.Task_9.hw_9_task_2 import ContextCls, context_gen
import pytest


def test_class_suppressed_passed_exception():
    with ContextCls(IndexError):
        [][2]


def test_generator_suppressed_passed_exception():
    with context_gen(IndexError):
        [][2]


def test_class_not_suppressed_exception():
    with pytest.raises(ZeroDivisionError):  # noqa:
        with context_gen(IndexError):
            1 / 0


def test_generator_and_class_supressed_subclass_exceptions():
    with context_gen(Exception):
        raise IndexError()
    with context_gen(Exception):
        raise IndexError()


def test_generator_not_suppressed_exception():
    with pytest.raises(ZeroDivisionError):  # noqa:
        with context_gen(IndexError):
            1 / 0
