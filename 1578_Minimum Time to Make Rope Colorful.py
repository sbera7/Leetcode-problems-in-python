class Solution(object):
    def minCost(self, colors, neededTime):
        colors = list(colors)
        if len(colors) < 2:
            return 0

        l, r, res = 0, 1, 0
        while True:
            if r > len(colors) - 1:
                break

            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res = res + neededTime[l]
                    del neededTime[l]
                    del colors[l]

                else:
                    res = res + neededTime[r]
                    del neededTime[r]
                    del colors[r]

            else:
                l, r = l + 1, r + 1
            
        return res
