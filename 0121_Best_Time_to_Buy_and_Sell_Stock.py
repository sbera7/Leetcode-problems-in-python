class Solution:
    def maxProfit(self, prices) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            maxP = max(maxP, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxP
