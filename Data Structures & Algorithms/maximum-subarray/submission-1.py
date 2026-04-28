class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = None
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += n
            print(curr_sum)
            if not res:
                res = curr_sum
            else:
                res = max(res, curr_sum)

        return res