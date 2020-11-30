def find_maximum_and_minimum(numbers: str):
    with open(numbers, "r") as f:
        nums = f.read().splitlines()
    result = sorted(nums)
    return int(result[0]), int(result[-1])
