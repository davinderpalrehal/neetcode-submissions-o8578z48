class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        
        cache = {}
        
        def explore(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if text1[i] == text2[j]:
                res = 1 + explore(i + 1, j + 1)
            else:
                res = max(explore(i + 1, j), explore(i, j + 1))
            
            cache[(i, j)] = res
            return res
        
        return explore(0, 0)