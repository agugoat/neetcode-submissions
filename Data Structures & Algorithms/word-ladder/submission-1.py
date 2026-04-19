class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)

        # compute wildcard patterns
        for word in wordList:
            for i in range(len(word)):
                new_str = word[:i] + '*' + word[i+1:]
                graph[new_str].append(word)
        
        # run bfs
        queue = deque([beginWord])
        visit = set([beginWord])

        count = 1
        while queue:

            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return count            
                
                
                for i in range(len(curr)):
                    string = curr[:i] + '*' + curr[i+1:]
                    for new_word in graph[string]:
                        if new_word not in visit:
                            visit.add(curr)
                            queue.append(new_word)
                    graph[string] = []
            count +=1
        return 0


        # time = O( n * L)













        