class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pf = [0] * n
        pf[-1] = -1

        for j in range(n-2, -1, -1):
            pf[j] = max(pf[j+1], prices[j+1])

        maxv = 0
        for i in range(n):
            maxv = max(maxv, pf[i] - prices[i])

        return max(maxv, 0)