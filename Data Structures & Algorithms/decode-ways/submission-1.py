class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        dp = (n+1) * [0]
        
        # set base case
        dp[0] = 1

        for i in range(1,n+1):
            
            single = int(s[i-1])

            if single >= 1:
                dp[i] += dp[i-1]

            if i >= 2:
                two_digits = int(s[i-2:i])
                if two_digits >= 10 and two_digits <= 26:
                    dp[i] += dp[i-2]
        
        return dp[n]
            







        