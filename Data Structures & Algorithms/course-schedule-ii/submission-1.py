class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = numCourses * [0]
        graph = defaultdict(list)
        queue = deque()

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegrees[course] += 1
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)  
        print(graph)
        print(indegrees)
        print(queue)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        
        return res if len(res) == numCourses else []


        