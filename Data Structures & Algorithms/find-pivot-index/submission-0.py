class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i, n in enumerate(nums):
            if left == right - n:
                return i
            left += n
            right -= n
        
        return -1