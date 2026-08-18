class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        return len(a) != len(nums)
        