class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            else:
                if len(stack) > 0 and stack[-1] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0