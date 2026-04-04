class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)

        for i in range(N - 1):
            biggest = -1
            for j in range(i + 1, N):
                biggest = max(arr[j], biggest)
            arr[i] = biggest
        
        arr[-1] = -1

        return arr