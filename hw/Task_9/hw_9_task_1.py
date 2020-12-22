"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""


from typing import List, Iterator, Generator, Optional


def get_value_from_file(path: str) -> int:
    with open(path) as f:
        for line in f:
            yield int(line)


def get_next_from_iterator(iterator: Generator) -> Optional[int]:
    try:
        value = next(iterator)
    except StopIteration:
        value = None
    return value


def merge_sorted_files(file_list: List[str]) -> Iterator:

    first_f = get_value_from_file(file_list[0])
    second_f = get_value_from_file(file_list[1])
    first_turn = next(first_f)
    second_turn = next(second_f)

    while True:
        if first_turn is None and second_turn is None:
            break

        elif second_turn is None:
            yield first_turn
            first_turn = get_next_from_iterator(first_f)

        elif first_turn is None:
            yield second_turn
            second_turn = get_next_from_iterator(second_f)

        elif first_turn < second_turn:
            yield first_turn
            first_turn = get_next_from_iterator(first_f)
        else:
            yield second_turn
            second_turn = get_next_from_iterator(second_f)
