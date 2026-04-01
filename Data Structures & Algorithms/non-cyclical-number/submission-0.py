class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num, seen):
            num_str = str(num)
            res = 0

            for c in num_str:
                res += (int(c) ** 2)
            
            if res in seen:
                return False
            seen.add(res)

            if res == 1:
                return True
            
            return helper(res, seen)
        
        seen = set()
        return helper(n, seen)