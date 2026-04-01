# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def helper(pairs, s, e):
            if e - s + 1 <= 1:
                return
            
            pivot = pairs[e]
            left = s
            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[i], pairs[left] = pairs[left], pairs[i]
                    left += 1
            
            pairs[left], pairs[e] = pairs[e], pairs[left]
            helper(pairs, s, left - 1)
            helper(pairs, left + 1, e)
        
        helper(pairs, 0, len(pairs) - 1)
        return pairs