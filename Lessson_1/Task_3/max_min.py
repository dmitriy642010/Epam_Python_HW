
class Min_max():
    def __init__(self):
        pass
    def find_maximum_and_minimum(self, numbers: str):
        with open(numbers, 'r') as f:           #here we read from a file we setup
            nums = f.read().splitlines()
            for i, elem in enumerate(nums):     #need to transfer from str to int
                nums[i] = int(elem)
               #returning list of integers

        result = sorted(nums)                   #we sort the list of integers to take the fisrt and last result for min and max
        return result[0], result[-1]

resultat = Min_max()
print(resultat.find_maximum_and_minimum("numbers.txt"))