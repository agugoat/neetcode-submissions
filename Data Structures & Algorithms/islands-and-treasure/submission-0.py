class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n = len(grid)
        m = len(grid[0])
        queue = deque()
        INF = 2147483647

        # loop through the graph and change it
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i,j))

        # run that multi - bfs        
        while queue:
            i , j = queue.popleft()
            for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr , nc = dr + i , dc + j

                if ((0 <= nr < n) and (0 <= nc < m)) and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[i][j] + 1
                    queue.append((nr,nc))



        '''
        input: grid with stuff
        output: grid updated in place

        example:
         [0,-1],
         [2147483647,2147483647]

          final:
          [0,-1],
          [1,2]

        [0,2147483647],
        [2147483647,2147483647]
        final:
        [0,1],
        [1,2]

        potienal solutions:
        using bfs to go level by level
        time - O(n * m) , space = O(1)
        dfs is possible not clear rn to me

        pesdudocode-

        1. go through the graph , change every 0 to like or something to make it clear

        2. from those points run bfs and everytime u see like inf keep the lowest distance

        3. after that we change those Xs back to 0s and we should have our ting 


        '''
        