class Solution:
    def romanToInt(self, s: str) -> int:
        sym_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        # s = XLIX
        i = len(s) - 1
        while i > -1: # [3,2,1,0] - 2
            # s[2] -> I
            # s[1] -> L
            # sym_map[s[i]] -> sym_map[s[2]] -> 1
            # sym_map[s[i-1]] -> sym_map[s[1]] -> 50
            res += sym_map[s[i]] # res = -1 + 10 = 9 + 
            if i - 1 > -1 and sym_map[s[i]] > sym_map[s[i - 1]]:
                res -= sym_map[s[i-1]] # res = 0 - 1 = -1
                i -= 1
            i -= 1

        return res