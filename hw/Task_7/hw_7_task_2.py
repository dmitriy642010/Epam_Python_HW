def backspace_compare(first: str, second: str):
    return backspace(first) == backspace(second)


def backspace(text: str) -> str:
    res = ''
    for x in text:
        if x == "#":
            res = res[:-1]
        else:
            res += x
    return res
