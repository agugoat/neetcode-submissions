class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        m = len(grid[0])
        seen = set()

        if grid[0][0] == 1:
            return -1
        
        q = deque()
        q.append((0,0,1))
        seen.add((0,0))

        while q:

            i , j, dist = q.popleft()

            if i == n-1 and j == m-1:
                return dist
            
            for dr, dc in [(0,1),(0,-1), (-1,0), (1,0), (-1,-1), (1,1), (1,-1), (-1,1)]:
                nr , nc = dr + i , dc + j

                if ((0 <= nr < n) and (0 <= nc < m)) and grid[nr][nc] == 0 and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    q.append((nr,nc, dist +1))
        
        return -1



        
        