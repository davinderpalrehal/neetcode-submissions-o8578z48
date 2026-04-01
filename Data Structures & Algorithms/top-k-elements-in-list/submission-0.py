class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for n in nums:
            num_count[n] += 1
        
        heap = []
        for n in num_count:
            heapq.heappush(heap, (-num_count[n], n))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res