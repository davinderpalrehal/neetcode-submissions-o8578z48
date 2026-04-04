class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)

        for i in range(N):
            nums.append(nums[i])
        
        return nums