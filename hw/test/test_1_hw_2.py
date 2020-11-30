import os
from typing import List

from ..Task_2.hw_2_task_1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    data_open,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

import pytest


@pytest.fixture()
def file_with_longest_diverse_words():
    file = "file_with_longest_diverse_words.txt"
    with open(file, "w") as f:
        f.write(
            "Es handelt sich um eine Kernfrage unserer Zeit, das hei\\u00dft,"
            "um eine Frage, die auf alle F\\u00e4lle Gef\\u00e4hrdung mit sich bringt."
        )
    yield file
    os.remove(file)


def test_get_longest_diverse_words(file_with_longest_diverse_words):
    actual_result = get_longest_diverse_words(file_with_longest_diverse_words)

    assert actual_result == [
        'Gefährdung',
        'Kernfrage',
        'handelt',
        'heißtum',
        'bringt',
        'unserer',
        'Frage',
        'Fälle',
        'sich',
        'Zeit',
    ]


@pytest.fixture()
def file_with_rarest_char():
    file = "file_with_rarest_chars.txt"
    with open(file, "w") as f:
        f.write("Es handelt sich um eine Kernfrage unserer Zeit, das hei\\u00dft,")
    yield file
    os.remove(file)


def test_get_rarest_char(file_with_rarest_char):
    actual_result = get_rarest_char(file_with_rarest_char)

    assert actual_result == "E"


@pytest.fixture()
def file_count_punctuation_chars():
    file = "file_with_punctuation.txt"
    with open(file, "w") as f:
        f.write(
            "Das  ist  ein  wichtiger  Unterschied.  Er  n\\u00e4hert  die,"
            "Fragen den Verh\\u00f6ren an. Man wird das an der Entwicklung verfol."
        )
    yield file
    os.remove(file)


def test_count_punctuation_chars(file_count_punctuation_chars):
    actual_result = count_punctuation_chars(file_count_punctuation_chars)

    assert actual_result == 4


@pytest.fixture()
def file_with_non_ascii_chars():
    file = "file_with_non_ascii_chars.txt"
    with open(file, "w") as f:
        f.write(
            """
           Der W\\u00e4hler also, an den wir denken, wird sich der Urnemit ganz anderen 
           Gef\\u00fchlen n\\u00e4hern als sein Vater oder Gro\\u00dfvater."""
        )
    yield file
    os.remove(file)


def test_count_non_ascii_chars(file_with_non_ascii_chars):
    actual_result = count_non_ascii_chars(file_with_non_ascii_chars)

    assert actual_result == 4


def test_get_most_common_non_ascii_char(file_with_non_ascii_chars):
    actual_result = get_most_common_non_ascii_char(file_with_non_ascii_chars)

    assert actual_result == "ä"
