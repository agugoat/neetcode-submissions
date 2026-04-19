class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # keep a k sized heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)

        # If we exceed size k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
