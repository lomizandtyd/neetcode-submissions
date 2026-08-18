class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
0,1 2,3, 4,5    3,4 -> [0,1], [2,3] [3,4] [4,5] -> [0,1] [2,5]
0,1 2,3   -1,0 -> [-1,1] [2,3]
0,1 3,4 2,5 -> [0,1] [2,5]
0,1 5,6 2,3 -> [0,1] [2,3] [5,6]
        """
        res = []
        i = 0

        # push left side
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # start merge
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        res.append(newInterval)

        # push right side
        while i < len(intervals):
            res.append(intervals[i])
            i+= 1
        return res
