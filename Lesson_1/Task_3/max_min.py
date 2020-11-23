def find_maximum_and_minimum(numbers: str):
    with open(numbers, "r") as f:  # here we read from a file we setup
        nums = f.read().splitlines()
        for i, elem in enumerate(nums):  # need to transfer from str to int
            nums[i] = int(elem)  # returning list of integers

    result = sorted(
        nums
    )  # we sort the list of integers to take the fisrt and last result for min and max
    return result[0], result[-1]
