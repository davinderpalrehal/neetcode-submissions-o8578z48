class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = []
        curr = None

        for _ in range(self.k):
            curr = -heapq.heappop(self.heap)
            temp.append(curr)
        
        for n in temp:
            heapq.heappush(self.heap, -n)
        
        return curr