class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []


        # first thing is to build the graph

        graph = {}
        # using zip to go through both arrays at the same time
        for (num , dem) , value in zip(equations,values):
            a , b = num , dem

            aSlashb = value
            bSlasha = 1/value

            if a not in graph:
                graph[a] = {}
            
            graph[a][b] = aSlashb

            if b not in graph:
                graph[b] = {}
            
            graph[b][a] = bSlasha
        
        print(graph)

        for (num,dem) in queries:
            a, b = num , dem

            if a not in graph or b not in graph:
                res.append(float(-1))
                continue
            
            if a == b:
                res.append(float(1))
                continue

            visited = set([a])

            resNum = self.dfs(graph,a,b,float(1),visited)

            if resNum:
                res.append(resNum)
            else:
                res.append(float(-1))
        
        return res


    def dfs(self,graph,source, destination, curramount, visited):
        
        # base case
        if source == destination:
            return curramount

        # loop through A : 20
        for neighbor, weight in graph[source].items():

            if neighbor not in visited:
                visited.add(neighbor)

                newprod = curramount * weight

                result = self.dfs(graph,neighbor,destination, newprod, visited)
                if result is not None:
                    return result
                visited.remove(neighbor)
        return None

        