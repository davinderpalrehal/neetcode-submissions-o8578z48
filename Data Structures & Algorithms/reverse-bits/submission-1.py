class Solution:
    def reverseBits(self, n: int) -> int:
        print(bin(n)[2:])
        n_str = bin(n)[2:]
        
        res = ''

        for c in n_str:
            res = c + res
        
        while len(res) < 32:
            res += '0'
        
        return int(res, 2)
