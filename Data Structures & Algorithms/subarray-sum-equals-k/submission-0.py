class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        curr_sum = 0
        res = 0
        prefix_sums = {0: 1}

        for r in range(N):
            curr_sum += nums[r]
            diff = curr_sum - k
            
            if diff in prefix_sums:
                res += prefix_sums[diff]
            
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
        return res