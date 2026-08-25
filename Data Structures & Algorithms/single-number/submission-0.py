class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]

        for nn in nums[1:]:
            n = n ^ nn

        return n
