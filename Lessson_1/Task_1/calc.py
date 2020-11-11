def check_power_of_2(a: int):
    if a == 0:
        return False
    return not (bool(a & (a - 1)))
