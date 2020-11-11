from typing import List


def find_maximal_subarray_sum(s: List[int], k: int) -> int:
    sub_start = 0
    sub_end = 0
    sub_sum = 0

    for i in s:
        sub_sum += i
        sub_end += 1

        while sub_sum > k:
            sub_sum -= s[sub_start]
            sub_start += 1

        summation = sub_end + sub_start

    return summation
