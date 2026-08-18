class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                ret.append(subset.copy())
                return

            dfs(i+1)
            subset.append(nums[i])
            dfs(i+1)
            subset.pop(-1)

        dfs(0)
        return ret

