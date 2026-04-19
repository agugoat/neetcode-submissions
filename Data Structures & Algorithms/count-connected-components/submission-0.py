class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()


        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        compos = 0

        for node in range(n):
            if node not in visited:
                compos +=1
                dfs(node)
               
        return compos

                

    



        