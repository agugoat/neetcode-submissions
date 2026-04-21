class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = numCourses * [0]

        graph = defaultdict(list)
        for course , preq in prerequisites:
            graph[preq].append(course)
        

        def dfs(node):
            
            if visit[node] == 1:
                return False
            
            if visit[node] == 2:
                return True

            visit[node] = 1

            for nei in graph[node]:    
                if not dfs(nei):
                    return False
            
            # node is full processed
            visit[node] = 2
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True
            
                    

                    

            


            
