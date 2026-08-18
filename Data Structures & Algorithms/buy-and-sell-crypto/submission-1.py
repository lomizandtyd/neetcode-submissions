class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        minBuy = prices[0]
        maxp = 0

        for sell in prices[1:]:
            maxp = max(sell - minBuy, maxp)
            minBuy = min(minBuy, sell)

        return maxp