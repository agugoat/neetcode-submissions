"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        '''
        brute force 
        loop through the interval , get the last element and do some type of comparesion to the 
        first element of the next interval, if the condtion ever breaks we return false
        '''
        
        # automatically sorts
        intervals.sort(key=lambda x: x.start)

        prev_end = None


        for inter in intervals:

            if prev_end is not None and prev_end > inter.start:
                return False
            
            prev_end = inter.end
        
        return True

        
