from typing import Any, Union


def find_occurrences(tree: Union[Any], element: Any) -> int:
    if not isinstance(tree, (list, tuple, dict, set)):
        return tree == element
    elif isinstance(tree, dict):
        iterator = tree.items()
    else:
        iterator = iter(tree)
    return sum(find_occurrences(x, element) for x in iterator)
