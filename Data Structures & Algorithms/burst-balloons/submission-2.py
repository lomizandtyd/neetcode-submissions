class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def dfs(arr):
            l = 1
            r = 1
            res = 0
            if len(arr) == 0:
                return 0

            arrt = tuple(arr)
            if arrt in cache:
                return cache[arrt]

            for i in range(0, len(arr)):
                l = arr[i-1] if i > 0 else 1
                r = arr[i+1] if i < len(arr) - 1 else 1
                res = max(res, l * r * arr[i] + dfs(arr[:i]+arr[i+1:]))
            # print(arr, res)
            cache[arrt] = res
            return res
            
        return dfs(nums)