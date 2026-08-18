class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mr = r

        while l+1 < r:

            m = (l + r + 1) // 2
            
            if self.canEat(piles, m, h):
                mr = m
                r = m
            else:
                l = m

        if self.canEat(piles, l, h):
            mr = l

        return mr


    def canEat(self, piles, m, h):
        cnt = 0
        for p in piles:
            cnt += p // m 
            if p % m > 0:
                cnt += 1

        return cnt <= h