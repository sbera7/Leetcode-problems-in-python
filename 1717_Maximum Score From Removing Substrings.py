class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def rem_ab(s):
            if len(s) == 0:
                return [], 0
            res = 0
            stack = [s[0]]
            for idx, ch in enumerate(s[1:]):
                if len(stack) == 0:
                    stack.append(ch)
                    continue
                if stack[-1] == 'a' and ch == 'b':
                    stack.pop()
                    res += x
                else:
                    stack.append(ch)
            
            return stack, res
        
        def rem_ba(s):
            if len(s) == 0:
                return [], 0
            res = 0
            stack = [s[0]]
            for idx, ch in enumerate(s[1:]):
                if len(stack) == 0:
                    stack.append(ch)
                    continue
                if stack[-1] == 'b' and ch == 'a':
                    stack.pop()
                    res += y
                else:
                    stack.append(ch)
            return stack, res
        
        if x > y:
            stack, res_1 = rem_ab(s)
            stack, res_2 = rem_ba(stack)
        else:
            stack, res_1 = rem_ba(s)
            stack, res_2 = rem_ab(stack)
        return res_1 + res_2
