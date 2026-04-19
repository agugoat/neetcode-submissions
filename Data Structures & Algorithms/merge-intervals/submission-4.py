class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        print(res)

        for i in range(1,n):
            curr_start, curr_end = intervals[i]
            last_start , last_end = res[-1]

            if last_end >= curr_start:
                res[-1] = [last_start ,max(last_end,curr_end)]
            else:
                res.append([curr_start,curr_end])
               
        
        return res
        '''
        input: intervals 
        output: list of combinted intervals

        example on paper
        edges: no interval 0s, empty

        apparoch: two choices check last of prevous interval and start of early one
        if beiiger append current enteval, if same or less append start of last and end of current

        pesduo code-

        1. go through the interval list , have the starting values of the first interval

        2. two choices if end of last is bigger than start of curr, append [start_last,end_curr] else
        append current

        3. update our varibles of the last one ig.
        '''
        