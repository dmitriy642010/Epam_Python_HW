from typing import List
import string


def data_open(file_path):
    with open(file_path) as f:
        file_path = bytes(f.read(), "ascii").decode("unicode-escape")
        return file_path


# print(data_open("data1.txt"))


def get_longest_diverse_words(file_path: str) -> List[str]:

    file = data_open(file_path)
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in file if ch not in exclude)
    data_set = text.split()
    data_set = sorted(data_set, key=lambda x: (-len(set(x)), -len(x)))

    return data_set[:10]


print(get_longest_diverse_words("data.txt"))


"""



def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:  
    """
