class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()

        def dfs(i, cur, total):
            nonlocal ret
            if i >= len(nums) or target < total:
                return

            if total == target:
                ret.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return ret