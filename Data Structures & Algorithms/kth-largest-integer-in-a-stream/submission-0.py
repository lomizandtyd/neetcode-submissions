class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []

        for v in nums:
            self.add(v)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)

        if len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]
