class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n= len(grid)
        m = len(grid[0])
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count+=1
                    self.dfs(grid,i,j)
        
        return count


    def dfs(self,grid, i, j):
        n= len(grid)
        m= len(grid[0])

        rowin = 0 <= i < n
        colin = 0 <= j < m
        if not (rowin and colin) or grid[i][j] == '0':
            return  # or like soemthing to be like we dont care

        grid[i][j] = '0'            
        
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            
            nr , nc = dr + i , dc + j
           
            self.dfs(grid,nr,nc)
        
        return None

        
        