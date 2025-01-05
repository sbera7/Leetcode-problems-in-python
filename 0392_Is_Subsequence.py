class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        for i in range(len(t)):
            if len(s) == sp:
                return True
            if s[sp] == t[i]:
                sp += 1

        if len(s) == sp:
            return True
        else:
            return False
