def find_maximum_and_minimum(numbers: str):
    with open(numbers, "r") as f:
        nums = f.read().splitlines()
        for i, elem in enumerate(nums):
            nums[i] = int(elem)

    result = sorted(nums)
    return result[0], result[-1]
