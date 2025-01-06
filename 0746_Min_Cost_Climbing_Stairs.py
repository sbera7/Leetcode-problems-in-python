class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        t0, t1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            new = cost[i] + min(t0, t1)
            t0 = t1
            t1 = new
        return min(t0, t1)
                
