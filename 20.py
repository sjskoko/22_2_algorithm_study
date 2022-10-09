class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() == match[i]:
                    pass
                else:
                    return False

        if stack:
            return False
        else:
            return True


'''
Runtime: 27 ms, faster than 98.47% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 26.38% of Python3 online submissions for Valid Parentheses.

'''