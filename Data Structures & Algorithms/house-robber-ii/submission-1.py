class Solution:
    def rob(self, nums: List[int]) -> int:
        """
[1] 0
[1 2]  2
[2 1 2] 2
[1 3 1] 3
[1 3 3 1] 4
[5 1 3 4] 8
        """

        if len(nums) <= 3:
            return max(nums)

        p0 = nums[0]
        p1 = nums[2] + p0
        pi = max(p0, p1)
        
        for i in range(3, len(nums)-1):
            pi = max(p1, p0+nums[i])
            p0, p1 = p1, pi

        p0 = nums[1]
        p1 = max(nums[2], p0)
        maxv = pi

        for i in range(3, len(nums)):
            pi = max(p0+nums[i], p1)
            p0, p1 = p1, pi

        maxv = max(pi, maxv)
        return maxv
        