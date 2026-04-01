class Solution:
    def isPalindrome(self, s: str) -> bool:
        r, l = len(s) - 1, 0

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True