class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def explore(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(
                explore(i + 1),
                nums[i] + explore(i + 2)
            )
            
            return cache[i]
        
        return explore(0)