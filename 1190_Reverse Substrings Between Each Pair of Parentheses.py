class Solution(object):
    def reverseParentheses(self, s):
        s = list(s)

        while '(' in s:
            for i, st in enumerate(s):
                if st == '(':
                    l = i
                if st == ')':
                    r = i
                    s[l:r+1] = reversed(s[l:r+1])
                    del s[r]
                    del s[l]
                    break
        return ''.join(s)
