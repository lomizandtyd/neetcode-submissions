class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        stat = [False] * n
        stat[-1] = True

        for i in range(n-1, -1, -1):
            if (i+nums[i])+1 >= n:
                stat[i] = True

            for k in range(i, i+nums[i]+1):
                if stat[k]:
                    stat[i] = True
                    break


        return stat[0]