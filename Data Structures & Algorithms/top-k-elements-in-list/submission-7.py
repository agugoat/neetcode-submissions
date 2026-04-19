class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        min_heap = []
        freq = Counter(nums)
        print(freq)

        # build minheap
        for num in freq:
            heapq.heappush(min_heap, (-freq[num], num))
        
        print(min_heap)
        res = []
        for _ in range(k):
            freq , num = heapq.heappop(min_heap)
            res.append(num)
        return res






        