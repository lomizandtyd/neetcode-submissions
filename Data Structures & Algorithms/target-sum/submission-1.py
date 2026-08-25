class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = [{} for i in nums]

        def dfs(i, t):
            nonlocal cache
            if i > len(nums):
                return 0

            if i == len(nums):
                if t == 0:
                    return 1
                else:
                    return 0

            if t in cache[i]:
                return cache[i][t]

            res = 0
            res = dfs(i+1, t-nums[i])
            res += dfs(i+1, t+nums[i])

            cache[i][t] = res
            return res

        return dfs(0, target)

