class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        minj = [1e9] * n
        minj[-1] = 0

        for i in range(n-1, -1, -1):
            for k in range(i, i+nums[i]+1):
                if k < n and minj[k] < 1e9:
                    minj[i] = min(minj[k]+1, minj[i])

        return minj[0]