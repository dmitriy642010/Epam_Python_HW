from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:

    if len(data) < 3 or data[0] != 0 or data[1] != 1:
        return False

    for i in range(2, len(data)):
        if data[i] != data[i - 1] + data[i - 2]:
            return False

    return True
