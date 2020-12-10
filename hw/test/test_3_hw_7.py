import pytest
from Epam_training_HW.hw.Task_7.hw_7_task_3 import tic_tac_toe_checker


board_1 = [["-", "-", "x"], ["o", "-", " o"], ["x", "o", "x"]]
board_2 = [["-", "-", "x"], ["o", "x", " o"], ["x", "o", "x"]]
board_3 = [["-", "-", "x"], ["o", "o", " o"], ["x", "o", "x"]]


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [(board_1, "unfinished"), (board_2, "x"), (board_3, "o")],
)
def test_tic_tac_toe(value, expected_result):
    assert tic_tac_toe_checker(value) == expected_result
