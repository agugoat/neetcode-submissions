class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0


        def dfs(i,j):

            if not ((0<=i<n) and (0<=j<m)) or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            for dr , dc in [(1,0),(-1,0), (0,1), (0,-1)]:
                nr , nc = i + dr , j + dc
                dfs(nr,nc)
        
        for i in range(n):
            for j in range(m):

                if grid[i][j] == '1':
                    count +=1
                    dfs(i,j)
        
        return count

        