"""
1  2  3  4
1  2  6  24
1  2  3  4

-1 -3 -2  5  -3
-1  3  6 30  90
-1 -3 -6 -30 -3


-1 -3 -2   0  5  -3
-1  3  6   0  5  0
           0  0  -3

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxv = pmax = pmin = nums[0]

        for n in nums[1:]:
            cmax = max(pmax*n, pmin*n, n)
            cmin = min(pmax*n, pmin*n, n)
            maxv = max(cmax, maxv)
            pmax, pmin = cmax, cmin

        return maxv