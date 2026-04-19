class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        n = len(nums)

        for i in range(n):
            heapq.heappush(min_heap,nums[i])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
        

        