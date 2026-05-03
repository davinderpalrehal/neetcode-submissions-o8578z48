class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        res = 1
        N = len(arr)

        for r in range(1, N):
            c = (arr[r-1] > arr[r]) - (arr[r-1] < arr[r])
            if c == 0:
                l = r
            elif r > 1 and c * prev_c != -1:
                l = r - 1
            res = max(res, r - l + 1)
            prev_c = c

        return res