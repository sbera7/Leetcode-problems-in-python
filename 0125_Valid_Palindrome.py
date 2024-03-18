class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s=""
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                new_s = new_s + i
        
        left, right = 0, len(new_s)-1
        
        if len(new_s) % 2 == 0: 
            for i in range(int(len(new_s) / 2)):
                if new_s[left] != new_s[right]:
                    return False
                left += 1
                right -= 1 
        
        else:
            for i in range(int(len(new_s) / 2)):
                if new_s[left] != new_s[right]:
                    return False
                left += 1
                right -= 1
            
        return True
