class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0] 



        def robber(arr):
            n = len(arr)
            print(n)
            if n == 0:
                return arr[0]
            if n == 1:
                return arr[0]
           
            dp = n * [0]
            dp[0] = arr[0]
            dp[1] = max(arr[1], arr[0])

            for i in range(2,n):
                dp[i] = max(arr[i] + dp[i-2], dp[i-1])
            
            return dp[-1]
            
        return max(robber(nums[:-1]), robber(nums[1:]))
        