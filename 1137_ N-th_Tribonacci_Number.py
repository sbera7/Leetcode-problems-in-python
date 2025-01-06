class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n < 3:
            return t[n]
        else:
            for i in range(3, n+1):
                res = sum(t)
                t[0], t[1], t[2] = t[1], t[2], res
            return res 
