from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:

    for line_num, line in enumerate(board):
        last_check = check_horizontal_line(board, line_num)
        if last_check != None:
            return last_check

    for line_num, line in enumerate(board):
        last_check = check_vertical_line(board, line_num)
        if last_check != None:
            return last_check

    last_check = check_diagonal_lines(board)
    return last_check


def check_horizontal_line(board, row_num):
    row_num = []
    for row_num in board[0]:
        if all(a == 'x' for a in row_num):
            return 'x'
        elif all(a == 'o' for a in row_num):
            return 'o'
    return check_list_contains_all_x_or_o(row_num)


def check_vertical_line(board, col_num):
    col_num = []
    for col_num in zip(board):
        if all(a == 'x' for a in col_num):
            return 'x'
        elif all(a == 'o' for a in col_num):
            return 'o'
    return check_list_contains_all_x_or_o(col_num)


def check_diagonal_lines(board):

    line_vals = []

    for count1, vert_line in enumerate(board):
        line_vals.append(vert_line[count1])
        count1 += 1
    check_val = check_list_contains_all_x_or_o(line_vals)
    if check_val != None:
        return check_val

    line_vals = []
    for count1, vert_line in enumerate(reversed(board)):
        line_vals.append(vert_line[count1])
        count1 += 1
    check_val = check_list_contains_all_x_or_o(line_vals)
    return check_val


def check_list_contains_all_x_or_o(elementlist):

    if is_list_of(elementlist, "x"):
        return "x wins!"
    if is_list_of(elementlist, "o"):
        return "o wins!"

    return "unfinished"


def is_list_of(elementlist, search_string):

    if elementlist.count(search_string) == len(elementlist):
        return True
