class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []
        res = []

        heapq.heapify(min_heap)

        for point in points:
            x , y = point
            distance = math.sqrt((x-0)**2 + (y-0)**2)
            print(distance)
            heapq.heappush(min_heap,(distance,point))
        
        for i in range(k):
            val , point = heapq.heappop(min_heap)
            res.append(point)
        
        return res

            




        