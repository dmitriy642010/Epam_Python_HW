class Poisk(object):
    def check_sum_of_four(self,a, b, c, d):
        sums ={}
        for i in a:
            for j in b:
                if i+j not in sums:
                    sums[i+j] = 1
                else:
                    sums[i+j] +=1
        n = 0
        for i in c:
            for j in d:
                if -1 * (i+j) in sums:
                    n+=sums[-1*(i+j)]
            return n

