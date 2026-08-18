class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        ret = []
        ret2 = {}
        h = []

        i = 0

        for q in sorted(queries):
            # push
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(h, (r-l+1, r))
                i += 1
        
            while h and h[0][1] < q:
                heapq.heappop(h)

            ret2[q] = h[0][0] if h else -1

        return [ret2[q] for q in queries]