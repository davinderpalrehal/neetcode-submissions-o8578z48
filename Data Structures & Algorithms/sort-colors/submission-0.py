class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]
        for n in nums:
            buckets[n] += 1
        
        j = 0
        for i, c in enumerate(buckets):
            for _ in range(j, j + c):
                nums[j] = i
                j += 1
        