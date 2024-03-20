class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        l, r = 0, 1
        res = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res
