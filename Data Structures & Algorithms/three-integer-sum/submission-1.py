class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        print(nums)
        nums.sort()
        print(nums)
        N = len(nums)

        for a in range(N - 2):
            if a > 0:
                if nums[a] == nums[a - 1]:
                    continue
            l, r = a + 1, N - 1
            while l < r:
                curr_sum = nums[a] + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res