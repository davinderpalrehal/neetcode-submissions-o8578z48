class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [1] * N
        prefix = 1
        postfix = 1

        for i in range(N):
            output[i] = prefix
            prefix *= nums[i]
        
        # Postfix
        for i in reversed(range(N)):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output