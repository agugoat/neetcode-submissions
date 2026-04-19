class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify_max(nums)

        for i in range(k-1):
            heapq.heappop_max(nums)
        
        return nums[0]

        # python 3.14 allows heapq.maxheap


      

        '''
        input: list of nums 
        output: the kth largest element

        basically run min heapify k times basically
        get the lowest element
        '''
        