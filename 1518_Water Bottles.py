class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = numBottles
        empty = numBottles
        while empty // numExchange:
            res = res + empty // numExchange
            left_emp = empty % numExchange
            empty = empty // numExchange + left_emp
        
        return res
