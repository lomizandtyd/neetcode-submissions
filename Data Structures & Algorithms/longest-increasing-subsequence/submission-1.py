class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n

        for j in range(1, n):
            for k in range(j-1, -1, -1):
                if nums[k] < nums[j]:
                    dp[j] = max(dp[j], dp[k]+1)

        return max(dp)
