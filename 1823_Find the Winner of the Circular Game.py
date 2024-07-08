class Solution(object):
    def findTheWinner(self, n, k):
        if n == 1:
            return 1
        init_list = [i+1 for i in range(n)]
        index =0
        while True:
            index = (index + k - 1) % len(init_list)
            del init_list[index]
            if len(init_list) == 1:
                break
        return init_list[0]
