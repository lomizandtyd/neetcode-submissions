"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda i: i.start)

        e = intervals[0].end

        i = 1
        while i < len(intervals):
            if intervals[i].start < e:
                return False
            else:
                e = intervals[i].end
            i += 1

        return True