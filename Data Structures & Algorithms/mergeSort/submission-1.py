# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        N = len(pairs)

        if N <= 1:
            return pairs
        
        m = N // 2

        def merge(arr1, arr2):
            p1 = p2 = 0
            res = []

            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1].key < arr2[p2].key:
                    res.append(arr1[p1])
                    p1 += 1
                else:
                    res.append(arr2[p2])
                    p2 += 1
            
            while p1 < len(arr1):
                res.append(arr1[p1])
                p1 += 1
            
            while p2 < len(arr2):
                res.append(arr2[p2])
                p2 += 1
            
            return res

        return merge(self.mergeSort(pairs[m:]), self.mergeSort(pairs[:m]))