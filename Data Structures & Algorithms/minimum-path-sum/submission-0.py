class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        print(dp)

        for i in range(m):
            dp[i][0] = grid[i][0]

            if i >= 1:
                dp[i][0] = grid[i][0] + dp[i-1][0]
                
        
        for j in range(n):
            dp[0][j] = grid[0][j]

            if j >= 1:
                dp[0][j] = grid[0][j] + dp[0][j-1]
                
        
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])
        
        return dp[m-1][n-1]
                



        '''
        input: grid with non negative ints
        output is the minimn path

        off the rip we can do this with a dp[i][j] grid where each stat is the 
        least amount to get to that path

        dp[i][j] = the amount of the min path which 
        dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        '''


        