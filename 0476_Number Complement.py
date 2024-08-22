class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 0
        req = 0
        while num:
            digit = 0 if num % 2 else 1
            req = req + digit * (2 ** n)
            n += 1
            num = num / 2
        
        return req
