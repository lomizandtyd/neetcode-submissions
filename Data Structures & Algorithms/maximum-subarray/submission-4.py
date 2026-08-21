class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxs = nums[0]
        curs = 0

        for n in nums:
            if curs <= 0:
                curs = 0
            curs += n
            maxs = max(curs, maxs)

        return maxs