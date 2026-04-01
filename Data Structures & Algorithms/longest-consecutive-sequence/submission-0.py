class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_dupes = list(set(nums))
        no_dupes.sort()
        res = 0
        last = 0

        print(no_dupes)

        for i in range(1, len(no_dupes)):
            if no_dupes[i] - no_dupes[i-1] > 1:
                res = max(res, i - last)
                last = i
        
        res = max(res, len(no_dupes) - last)

        return res