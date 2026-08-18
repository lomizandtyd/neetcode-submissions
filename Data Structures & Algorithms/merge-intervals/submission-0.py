class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        
        intervals.sort(key=lambda i: i[0])

        res = [intervals[0]]

        i = 1
        while i < len(intervals):
            while i < len(intervals) and res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
                i += 1

            while i < len(intervals) and res[-1][1] >= intervals[i][0]:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
                i += 1

        return res

            

