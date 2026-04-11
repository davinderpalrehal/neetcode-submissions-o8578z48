class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_distance(x, y):
            return (((0 - x) ** 2) + ((0 - y) ** 2)) ** 0.5
        
        heap = []

        for x, y in points:
            heapq.heappush(heap, (calc_distance(x, y), [x, y]))
        
        res = []

        for _ in range(k):
            _, point = heapq.heappop(heap)
            res.append(point)
        
        return res