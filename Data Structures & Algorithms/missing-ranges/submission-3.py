class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        missing_start = lower

        for num in nums:
            if num > missing_start:
                res.append([missing_start, num - 1])
            missing_start = num + 1

        if missing_start <= upper:
            res.append([missing_start, upper])

        return res