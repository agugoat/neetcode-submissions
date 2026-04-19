class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0 
        
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j):

            if not ((0 <= i < n) and (0 <= j < m)) or grid[i][j] == '0':
                return 

            # turn into 0
            grid[i][j] = '0'
            print(grid)
            # going in all 4 directions
            for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr , nc = dr + i , dc + j
                dfs(nr,nc)


                
        
        island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    island_count +=1
                    dfs(i,j)
        return island_count

                
                

        



        '''
        input: grid of 0s and 1s
        ouput: int of the number of numIslands

        example                  
        0110              0000
        0000              1111
        0010              1111
         2 islands       1 island

        edge cases:
        no islands -> return 0

        potential solutions:
        dfs  time complex = O(n * m) , space O(n * m)
        bfs would be same thing space would be len of queue

        pesduo code:

        1. loop through the grid , everytime we see a one we run dfs

        2. in dfs everytime we see a 1 we change it 0 within our udlr bounds

        3. until we see no more ones, then we add one to our island count

        4. by the end the grid is empty and we have the number of islands

        '''
        