class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        
        res = None
        for _ in range(k):
            res = -heapq.heappop(heap)
        
        return res