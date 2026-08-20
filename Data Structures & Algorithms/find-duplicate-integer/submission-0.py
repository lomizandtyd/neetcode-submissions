class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = 0

        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break

        i2 = 0
        while True:
            i2 = nums[i2]
            i = nums[i]
            if i2 == i:
                break
        return i