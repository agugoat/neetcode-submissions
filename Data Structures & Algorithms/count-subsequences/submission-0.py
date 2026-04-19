class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        '''
        include or dont include

        dp[i][j] = the number of subqeunces
        base case
        from an empty string there is one way to generate the needed string
        '''
        n = len(s)
        m = len(t)

        dp = [[0] * (m+1) for _ in range(n+1)]

        dp[0][0] = 1

        for i in range(1,n+1):
            dp[i][0] = 1
      
        
        # cook

        for i in range(1,n+1):
            for j in range(1,m+1):
                # include if match
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1] + dp[i-1][j]
                else: # skip
                    dp[i][j] += dp[i-1][j]
        
        print(dp)
        
        return dp[n][m]
    
        