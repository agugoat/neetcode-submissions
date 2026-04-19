class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []



        def bt(index,path):

            res.append(path[:])

            for i in range(index,n):
                # choose
                path.append(nums[i])

                #explore
                bt(i+1,path)

                #pop
                path.pop()
        
        bt(0,path)
        return res
        