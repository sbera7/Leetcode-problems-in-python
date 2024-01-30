class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort()
        if "" in strs:
            return ""
        result = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                break
        return result
