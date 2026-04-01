class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        k = hi

        def calc_time(m):
            time = 0 

            for p in piles:
                time += math.ceil(p / m) 
            
            return time

        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            time = calc_time(mid)

            if time > h:
                lo = mid + 1
            else:
                hi = mid - 1
                k = mid
        
        return k