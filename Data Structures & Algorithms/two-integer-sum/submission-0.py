class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3,4,5,6 -> 7
        diff = {}
        # {
        #   
        # }

        for i, n in enumerate(nums): # 0, 3
            if n in diff:
                return [diff[n], i]
            diff[target - n] = i 