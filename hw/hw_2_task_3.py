import itertools


def combi(*args):
    return list(itertools.product(*args))


print(combi([1, 2], [3, 4]))
