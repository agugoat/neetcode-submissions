class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * (n)
        suffix = [1] * (n)

        res = [0] * n



        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for j in range(n-2, -1 , -1):
            suffix[j] = nums[j+1] * suffix[j+1]

        for k in range(n):
            res[k] = prefix[k] * suffix[k]
        
        
        return res
        
       
        '''
        input : list of nums
        output: list of nums

        example:
        nums = [1,2,4,6]

        prefix = [1,1,2,8]
        suffix = [48,24,6,1]

        basically don't include that number

        basically we get the prefix from the left , excluding the current number we are on
        then we get the suffix from the right excluding each number

        and then if we multiply them together we should have the right number

        '''
        