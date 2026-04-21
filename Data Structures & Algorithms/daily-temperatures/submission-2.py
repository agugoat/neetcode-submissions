class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        stack = []
        res = n * [0]

        for i in range(n):
            curr = temperatures[i]
            while stack and curr > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            
            stack.append(i)

        return res        