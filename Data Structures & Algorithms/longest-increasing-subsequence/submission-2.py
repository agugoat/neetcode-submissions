class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        '''
        dp[i] represents the longest increasing subsequence at the time

        '''
        n = len(nums)


        dp = n * [1]


        for i in range(1,n):
            curr = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    curr = max(curr, dp[j] + 1)
                dp[i] = curr
                    
            
        print(dp)
        return max(dp)
        