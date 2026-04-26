class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            curr = i
            bits = 0
            while curr:
                bits += curr % 2
                curr = curr >> 1
            res.append(bits)
        
        return res
