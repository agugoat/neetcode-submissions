class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        path = []
        res = []
        n = len(nums)
        used = set()
        

        def bt():

            if n == len(path):
                res.append(path[:])
            

            for i in range(n):
                # choose
                if nums[i] not in used:
                    path.append(nums[i])
                    used.add(nums[i])
                
                    # explore
                    bt()
                    #backtrack
                    path.pop()
                    used.remove(nums[i])

        
        bt()
        return res