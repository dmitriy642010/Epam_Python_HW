def letter_range(start, stop="{", step=1):

    for ord_ in range(ord(start.lower()), ord(stop.lower()), step):
        yield chr(ord_)


print(list(letter_range("a", "f")))
