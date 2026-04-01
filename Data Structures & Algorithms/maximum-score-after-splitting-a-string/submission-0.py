class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0

        for c in s:
            if c == '0':
                left += 1
        
        res = 0

        for i in reversed(range(1, len(s))):
            if s[i] == '1':
                right += 1
            else:
                left -= 1
            res = max(res, right + left)

        return res