import string
from typing import List


def data_open(file_path):
    with open(file_path) as f:
        file = bytes(f.read(), "ascii").decode("unicode-escape")
        return file


def get_longest_diverse_words(file_path: str) -> List[str]:

    file = data_open(file_path)
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in file if ch not in exclude)
    data_set = text.split()
    data_set = sorted(data_set, key=lambda x: (len(set(x)), len(x)), reverse=True)
    return data_set[:10]


def get_rarest_char(file_path: str) -> str:
    text = data_open(file_path)
    d = {}
    for elem in text:
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] += 1
    res = [str(num) for num, count in d.items() if count == min(d.values())]
    return res[0]


def count_punctuation_chars(file_path: str) -> int:
    file = data_open(file_path)
    count = lambda l1, l2: sum([1 for x in l1 if x in l2])
    res = count(file, set(string.punctuation))
    return res


def count_non_ascii_chars(file_path: str) -> int:
    file = data_open(file_path)
    res = 0
    for elem in file:
        if ord(elem) > 128:
            res += 1
    return res


def get_most_common_non_ascii_char(file_path: str) -> str:
    file = data_open(file_path)
    chars = [ch for ch in file if ord(ch) > 128]
    chars_counter = {chars.count(val): val for val in set(chars)}
    return chars_counter[max(chars_counter.keys())]
