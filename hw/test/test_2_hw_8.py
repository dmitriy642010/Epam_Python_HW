from Epam_training_HW.hw.Task_8.hw_8_task_2 import TableData

import pytest


@pytest.fixture()
def presidents():
    return TableData(
        database_name="C:/Users/admin/Desktop/Epam_git_env/Epam_training_HW/hw/test/example.sqlite",
        table_name="presidents",
    )


def test_len(presidents):
    assert len(presidents) == 3


def test_get_item(presidents):
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains(presidents):
    assert ("Yeltsin" in presidents) is True
    assert ("Washington" in presidents) is False


def test_iter(presidents):
    names = [president[0] for president in presidents]
    assert names == ["Yeltsin", "Trump", "Big Man Tyrone"]
