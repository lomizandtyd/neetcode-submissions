class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-i for i in stones]
        heapq.heapify(q)

        while len(q) >= 2:
            m1 = -heapq.heappop(q)
            m2 = -heapq.heappop(q)

            if m1 != m2:
                delta = m1 - m2
                heapq.heappush(q, -delta)
            
        return 0 if not q else -q[0]