class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        p0 = 0
        p1 = nums[0]
        p2 = nums[1]
        

        for i in range(2, len(nums)):
            pi = max(p0+nums[i], p1 + nums[i], p2)
            p0, p1, p2 = p1, p2, pi

        return max(pi, p0, p1, p2)