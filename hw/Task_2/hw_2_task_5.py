from typing import Any, List, Sequence
import string


def check_steps(ind_start: int, ind_stop: int, step: int) -> bool:
    if step > 0 and ind_start >= ind_stop:
        return False
    elif step < 0 and ind_start <= ind_stop:
        return False
    else:
        return True


def custom_range(
    seq: Sequence, start: Any, stop: Any = None, step: Any = None
) -> List[Any]:
    if stop is None:
        stop = start
        start = seq[0]

    if step is None:
        step = 1

    res = []

    while True:
        ind_start = seq.index(start)
        ind_stop = seq.index(stop)

        if not check_steps(ind_start, ind_stop, step):
            break
        else:
            res.append(seq[ind_start])
            next_ind = ind_start + step
            if next_ind < 0 or next_ind > seq.index(seq[-1]):
                break
            start = seq[next_ind]
    return res
