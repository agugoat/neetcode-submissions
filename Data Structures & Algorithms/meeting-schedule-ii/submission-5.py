"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        # build a list i can acutally do stuff with and sort it
           # automatically sorts
        intervals.sort(key=lambda x: x.start)

        min_heap = []

        # Add the first meeting's end time
        heapq.heappush(min_heap, intervals[0].end)


        for inter in intervals[1:]:

            # If the earliest room to get free is free before this meeting starts,
            # we can reuse that room.
            if min_heap[0] <= inter.start:
                heapq.heappop(min_heap)  # free that room

            # Allocate current meeting (either reused or new room)
            heapq.heappush(min_heap, inter.end)
        
        return len(min_heap)
           

      
