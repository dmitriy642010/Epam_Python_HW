import collections
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    elements = collections.Counter(inp).most_common()
    maximum = elements[0][0]
    minimum = elements[-1][0]
    return maximum, minimum
