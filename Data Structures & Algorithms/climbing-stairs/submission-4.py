class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        
        if n == 2:
            return 2

        dp = [0] * n 

        # we know that there is one way to get to 1
        # and there is 2 ways to get to 2
        dp[0] = 1
        dp[1] = 2

        for i in range(2,n):
            dp[i] = (dp[i-1]  + dp[i-2] )

        return dp[n-1]
        