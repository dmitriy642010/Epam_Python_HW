from typing import Any, Union


def find_occurences(
    tree: Union[str, list, tuple, dict, set, int, bool], element: Any
) -> int:
    if not isinstance(tree, (list, tuple, dict, set)):
        return tree == element
    elif isinstance(tree, dict):
        iterator = tree.items()
    else:
        iterator = iter(tree)
    return sum(find_occurences(x, element) for x in iterator)
