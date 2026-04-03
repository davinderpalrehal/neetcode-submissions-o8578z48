class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = []

        for s in stones:
            heapq.heappush(stones_heap, -s)

        while len(stones_heap) > 1:
            x = -heapq.heappop(stones_heap)
            y = -heapq.heappop(stones_heap)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones_heap, -(y - x))
            else:
                heapq.heappush(stones_heap, -(x - y))
        
        return -stones_heap[0] if len(stones_heap) else 0