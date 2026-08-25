"""
maxp  0    2
           
pos   1    1    1    0    0


K = min


maxp(n) = maxp(K-2) + sale(n) - min

state:
    sale
    hold

    maxp(n) = max(maxp(n-1), 
        maxb + sale
    )

    maxb(n) = max(maxb(n-1), 
        maxp(n-2) - td
    )

           1    3    4    0    4    3    1
maxp 0  0  0    2    3    3    6    6    
maxb M  M  -1   -1   -1   2    2    

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) + 2
        maxp = [0] * n
        maxb = [0] * n
        maxb[0] = maxb[1] = -1e9

        for pi, p in enumerate(prices):
            k = pi + 2
            maxp[k] = max(maxp[k-1], maxb[k-1] + p)
            maxb[k] = max(maxb[k-1], maxp[k-2] - p)

        return maxp[-1]
