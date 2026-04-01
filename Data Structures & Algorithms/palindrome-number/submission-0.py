class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        N = len(num_str)
        l, r = 0, N - 1

        while l < r:
            if num_str[l] != num_str[r]:
                return False
            l += 1
            r -= 1
        
        return True