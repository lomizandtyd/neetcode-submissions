class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        p0 = nums[0]
        p1 = max(p0, nums[1])
        

        for i in range(2, len(nums)):
            pi = max(p0+nums[i], p1)
            p0, p1 = p1, pi

        return pi