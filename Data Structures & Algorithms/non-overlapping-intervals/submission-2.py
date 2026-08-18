class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i[0])

        pe = intervals[0][1]
        count = 0

        for s, e in intervals[1:]:
            # print(s, e, pe, count)
            if s < pe:
                pe = min(pe, e)
                count += 1
            else:
                pe = e

        return count