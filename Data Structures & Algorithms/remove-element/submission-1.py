class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)

        for i in range(N):
            if nums[i] == val:
                j = i
                while j < N and nums[j] == val:
                    j += 1
                if j == N:
                    return i
                nums[i], nums[j] = nums[j], nums[i]
        
        return N