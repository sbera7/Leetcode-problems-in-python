class Solution(object):
    def tribonacci(self, n):
        a, b, c = 0, 1, 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        for i in range(n-2):
            d = a + b + c
            c, b, a = d, c, b
        
        return d
