class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        k = max(piles)

        def calc_time(m):
            time = 0

            for p in piles:
                time += math.ceil(p / m)
            
            return time

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            time_to_eat = calc_time(mid)

            if time_to_eat <= h:
                k = min(k, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        
        return k