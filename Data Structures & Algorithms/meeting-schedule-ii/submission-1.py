"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda i: i.start)
        meeting_room = [intervals[0].end]

        for m in intervals[1:]:
            if meeting_room[0] <= m.start:
                merge = heapq.heappop(meeting_room)
                heapq.heappush(meeting_room, m.end)
            else:
                heapq.heappush(meeting_room, m.end)

        return len(meeting_room)