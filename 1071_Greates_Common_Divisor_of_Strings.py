class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            temp = str1
            str1 = str2
            str2 = temp
        temp_list = []
        res = ""
        for i in range(len(str2)):
            if len(str1) % (i + 1) != 0:
                continue
            if (str2[0 : i + 1] * int(len(str1) / (i + 1)) == str1) and (str2[0 : i + 1] * int(len(str2) / (i + 1)) == str2):
                res = str2[0 : i + 1]
        return res
