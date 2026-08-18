class MedianFinder:

    def __init__(self):
        self.lh = []
        self.rh = []

    def addNum(self, num: int) -> None:
        if len(self.lh) == 0:
            self.lh.append(-num)
            return

        lm = - self.lh[0]

        isOdd = len(self.lh) == len(self.rh)

        if num >= lm:
            heapq.heappush(self.rh, num)
        else:
            heapq.heappush(self.lh, -num)

        while len(self.lh) < (len(self.rh) ):
            heapq.heappush(self.lh, -self.rh[0])
            heapq.heappop(self.rh)

        while (len(self.rh)) < (len(self.lh) - 1):
            heapq.heappush(self.rh, -self.lh[0])
            heapq.heappop(self.lh)


    def findMedian(self) -> float:
        if len(self.lh) == 0:
            return 0.0
        # print(len(self.lh), len(self.rh))
        if len(self.lh) == len(self.rh):
            return (-self.lh[0] + self.rh[0]) / 2.0
        else:
            return -self.lh[0]
        
        