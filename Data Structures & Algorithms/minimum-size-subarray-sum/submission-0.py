class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        l = 0
        N = len(nums)
        res = N
        curr = 0

        for r in range(N):
            curr += nums[r]
            while curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
                
        return res