class Solution(object):
    def numTeams(self, rating):
        res = 0
        n = len(rating)
        for i in range(1, n):
            ls = lg = rs = rg = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    ls += 1
                else:
                    lg += 1
            for j in range(i + 1, n):
                if rating[j] < rating[i]:
                    rs += 1
                else:
                    rg += 1
            res += (ls * rg) + (rs * lg)
        return res
