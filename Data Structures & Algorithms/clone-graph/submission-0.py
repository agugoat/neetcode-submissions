"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        graph = defaultdict(list)


        def dfs(node):

            if node in graph:
                return graph[node]
            
            clone = Node(node.val)

            # making a copy
            graph[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            # bubble it up
            return clone
        
        print(graph)
        return dfs(node)
        




        