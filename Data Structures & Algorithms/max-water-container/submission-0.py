class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        res = 0
        l, r = 0, N - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return res