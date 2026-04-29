class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        # Standard Kadane's for max subarray sum
        max_res = nums[0]
        curr_max = 0
        # Standard Kadane's for min subarray sum
        min_res = nums[0]
        curr_min = 0

        for n in nums:
            curr_max = max(n, curr_max + n)
            max_res = max(max_res, curr_max)
            
            curr_min = min(n, curr_min + n)
            min_res = min(min_res, curr_min)
        
        # If all numbers are negative, total_sum == min_res, return max_res
        if max_res < 0:
            return max_res
            
        return max(max_res, total_sum - min_res)