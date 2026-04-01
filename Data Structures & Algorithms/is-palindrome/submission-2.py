class Solution:
    def isPalindrome(self, s: str) -> bool:
        r, l = len(s) - 1, 0
        ignore_list = set([' ', '?', '.', ',', "'", ':'])

        while l < r:
            if s[l] in ignore_list:
                l += 1
                continue
            if s[r] in ignore_list:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True