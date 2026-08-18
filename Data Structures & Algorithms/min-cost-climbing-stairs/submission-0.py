class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p0 = cost[0]
        p1 = cost[1]

        if len(cost) <= 2:
            return min(cost)

        min_cost = 1e12


        for i in range(2, len(cost)):
            pi = min(p0, p1) + cost[i]
            p0, p1 = p1, pi

        return min(pi, p0)