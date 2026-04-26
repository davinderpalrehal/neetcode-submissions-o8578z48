class Solution:
    def reverseBits(self, n: int) -> int:
        print(bin(n)[2:])
        n_str = bin(n)[2:]

        while len(n_str) < 32:
            n_str = '0' + n_str
        
        res = ''

        for c in n_str:
            res = c + res
        
        return int(res, 2)
