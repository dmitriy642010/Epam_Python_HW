import os

import pytest
from ..hw.Task_4.hw_4_task_1 import read_magic_number


@pytest.fixture()
def file_name(text: str):
    filename = "data.txt"
    with open(filename, "w") as f:
        f.write(text)
    yield filename
    os.remove(filename)


@pytest.mark.parametrize(
    ("text"),
    [
        ("1"),
        ("2"),
    ],
)
def test_correct_num(file_name):
    actual_result = read_magic_number(file_name)

    assert actual_result is True


@pytest.mark.parametrize(
    ("text"),
    [
        ("3"),
        ("0"),
    ],
)
def test_incorrect_num(file_name):
    actual_result = read_magic_number(file_name)

    assert actual_result is False


@pytest.mark.parametrize(
    ("text"),
    [
        ("That's an error"),
        ("And this too"),
    ],
)
def test_file_not_found_error(file_name):
    with pytest.raises(FileNotFoundError, match="No file was found!"):
        read_magic_number("no_file.txt")


def test_value_error(file_name):
    with pytest.raises(ValueError, match="Should be number here!"):
        read_magic_number(file_name)
