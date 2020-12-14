import itertools
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    def check_win(row: List):
        if all(map(lambda x: x == "x", row)):
            return "x"
        elif all(map(lambda x: x == "o", row)):
            return "o"
        return False

    all_lines_to_check_win = (
        board
        + [[board[i][j] for i in range(3)] for j in range(3)]
        + [[board[i][i] for i in range(3)]]
        + [[board[i][2 - i] for i in range(3)]]
    )

    for line in all_lines_to_check_win:
        if check_win(line):
            return f"{check_win(line)} wins!"

    if "-" in itertools.chain(*board):
        return "unfinished"

    return "draw!"
