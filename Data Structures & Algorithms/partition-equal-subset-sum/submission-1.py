class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        # sum(k) == total // 2
        # tgtsum(K) == total // 2
        #           ==   tgtsum(K-1) == total//2 - num[k]
        #           or   tgtsum(K-1) == total//2

        tgt = total // 2
        dp = [False] * (tgt+1)
        dp[0] = True

        for i in nums:
            for j in range(tgt, i - 1, -1):
                dp[j] = dp[j] or dp[j-i]
        return dp[tgt]