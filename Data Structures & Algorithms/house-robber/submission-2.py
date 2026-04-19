class Solution:
    def rob(self, nums: List[int]) -> int:



        n = len(nums)

        if n <=1:
            return nums[0]

        dp = n * [0]

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])


        for i in range(2,n):
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1])
        print(dp)
        return max(dp)



        '''
        input: is a list of numbers 
        output: is the max amount of money I can rob

        example:
        nums = [1,2,3,4]
        output -> 2 + 4 = 6

        nums = [2,9,8,3,6]
        nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16
        
        base case:
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        what would dp[i] represent? 
        dp[i] = dp[i-2] + nums[i]
        loop through and return the highest
        '''
        