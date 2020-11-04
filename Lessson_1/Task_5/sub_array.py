class Sub_array():
    def max_length(self,s, k):

        sub_start = 0
        sub_end = 0
        sub_sum = 0

        for i in s:
            sub_sum += i
            sub_end += 1

            while sub_sum > k:
                sub_sum -= s[sub_start]
                sub_start += 1

            summation = sub_end + sub_start

        return summation
prikol = Sub_array()

print(prikol.max_length([7, 4, -15, -4, 9, 2, 6, -1],5))