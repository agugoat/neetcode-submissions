class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
# 1. Condition Check: Correct Number of Edges
        # For a graph with 'n' nodes to be a tree, it MUST have exactly 'n-1' edges.
        # If len(edges) > n-1, it must contain a cycle.
        # If len(edges) < n-1, it must be disconnected.
        # We handle the 'disconnected' case later with len(visit) == n.
        if len(edges) > (n-1):
            return False
        # 2. Build the Adjacency List (Graph)
        graph = [[] for _ in range(n)]
        
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)


        # We only need to check for a cycle since the edge count check handles the rest.
        visit = set()

        def dfs(node, parent):

            if node in visit:
                return False   # cycle detected
            
            visit.add(node)

            for nei in graph[node]:
                # skip the back-edge
                if nei == parent:
                    continue
                
                # find cycle down a path
                if not dfs(nei,node):
                    return False
            
            return True
        
        #4. Final Result
        
        # A valid tree must:
        # a) Not contain a cycle (checked by dfs(0, -1)).
        # b) Be fully connected (checked by len(visit) == n).
        #    Since we already established len(edges) == n-1, if the graph is connected,
        #    it must be a tree. If it is NOT connected (len(visit) < n), the DFS 
        #    will not reach all nodes, and the function will return False, as desired. 
        return dfs(0, -1) and len(visit) == n


        