class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = nums[0]
        curs = 0

        for n in nums:
            curs += n
            maxs = max(curs, maxs)

            if curs <= 0:
                curs = 0
        
        return maxs