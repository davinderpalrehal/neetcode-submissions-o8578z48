class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(step):
            if step in cache:
                return cache[step]
            if step > n:
                return 0
            if step == n:
                return 1
            
            cache[step] = climb(step + 1) + climb(step + 2)
            return cache[step]
        
        return climb(0)