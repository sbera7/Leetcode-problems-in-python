class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1={}
        dict2={}
        for i in s:
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] = dict1[i] + 1
        for i in t:
            if i not in dict2.keys():
                dict2[i] = 1
            else:
                dict2[i] = dict2[i] + 1
        for i in dict1.keys():
            if i not in dict2.keys():
                return False
            if dict1[i] != dict2[i]:
                return False
        return True
