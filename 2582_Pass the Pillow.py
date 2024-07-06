class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        mod_val = time % ((n - 1) * 2)
        if mod_val < n:
            return mod_val + 1
        else:
            return n * 2 - mod_val - 1
