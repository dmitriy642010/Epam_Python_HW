def is_armstrong(number: int) -> bool:
    length = len(str(number))
    res = sum(x ** length for x in map(int, str(number)))
    return number == res
