class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegrees = defaultdict(int)
        queue = deque()

        for course , preq in prerequisites:
            graph[preq].append(course)
            indegrees[course] +=1
        # count the number of indegrees
        for i in range(numCourses):
            if not indegrees[i]:
                indegrees[i] = 0
                queue.append(i)
        
        
        # run khans algorithm
        count = 0
        while queue:
            node = queue.popleft()
            
            #for each processed node
            count +=1

            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        print(count)
        
        return count == numCourses
        


        




        