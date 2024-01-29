class Solution:
    def romanToInt(self, s: str) -> int:
        symList = { "I": 1, 
                    "IV": 4, 
                    "V": 5,
                    "IX": 9, 
                    "X": 10, 
                    "XL": 40, 
                    "L": 50, 
                    "XC": 90, 
                    "C": 100, 
                    "CD": 400,
                    "D": 500, 
                    "CM": 900, 
                    "M": 1000}

        res = 0

        for i in range(len(s)):
            if i == len(s) - 1:
                res += symList[s[i]]
            elif symList[s[i]] < symList[s[i+1]]:
                res -= symList[s[i]]
            else:
                res += symList[s[i]]
        
        return res
