class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if count[n] > count[res]:
                res = n

        return res