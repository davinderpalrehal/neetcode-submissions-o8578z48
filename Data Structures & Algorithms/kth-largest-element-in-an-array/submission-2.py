class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        k = N - k

        def quickSelect(l, r):
            while True:
                pivot, p = nums[r], l

                for i in range(l, r):
                    if nums[i] <= pivot:
                        nums[p], nums[i] = nums[i], nums[p]
                        p += 1
                
                nums[p], nums[r] = nums[r], nums[p]
                if p == k:
                    return nums[p]
                elif p > k:
                    r = p - 1
                else:
                    l = p + 1
        
        return quickSelect(0, N - 1)