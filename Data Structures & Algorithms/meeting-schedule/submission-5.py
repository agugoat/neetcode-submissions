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

        old_end = 0

        # build a list i can acutally do stuff with and sort it
        tup_list = []

        for i,time in enumerate(intervals):
            tup_list.append((time.start,time.end))
        
        print(tup_list)

        int_list=(sorted(tup_list))

        old_time = 0
        meeting = True
        for i , time in enumerate(int_list):
            start , end = time
            
            if i == 0:
                old_time = end
                continue
            
            if old_time > start:
                meeting = False
            
            # critical fr 
            old_time = end
            
        return meeting








