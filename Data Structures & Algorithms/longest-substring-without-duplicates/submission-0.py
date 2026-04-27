class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        N = len(s)
        l = 0
        res = 0

        for r in range(N):
            c = s[r]
            seen[c] += 1
            while seen[c] > 1:
                d = s[l]
                seen[d] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res