/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
    
      if (intervals == null || intervals.size() == 0) {
            return true;
        }

    intervals.sort(Comparator.comparingInt(interval -> interval.start));

    for(int i= 1; i < intervals.size(); i++) {

          Interval one = intervals.get(i);
          Interval tow = intervals.get(i-1);

          if(one.start < tow.end) {
            return false;
          }
    }
    return true;

}
}
