class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. find the minmal idx of the array
        # 2. binary search on its left and its right
        pos = self.find_minimal(nums)
        print(pos)
        l = self.binary_search(nums, 0, pos, target)
        print(l)
        if l != -1:
            return l

        r = self.binary_search(nums, pos, len(nums), target)
        print(r)
        return r


    def find_minimal(self, nums):
        l = 0
        r = len(nums)-1

        while l < r:
            m = l + (r - l ) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l

    def binary_search(self, nums, l, r, target):
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m+1
            elif nums[m] == target:
                return m
            else:
                r = m
        return -1