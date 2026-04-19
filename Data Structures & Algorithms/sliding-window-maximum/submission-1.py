class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = deque()

        for i in range(n):

            # remove elements that are smaller than the current element
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # add our current indices
            q.append(i)

            # remove from the front window
            if q and q[0] == i - k:
                q.popleft()

            # if the window is atleast size k , add it to the result
            if i >= k-1:
                res.append(nums[q[0]])
            
        
        return res