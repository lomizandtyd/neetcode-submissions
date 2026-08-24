class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        i = 0

        for i, dis in enumerate(nums):

            if i <= farest:
                farest = max(farest, i + dis)

            if farest >= len(nums) - 1:
                return True

        return False

            