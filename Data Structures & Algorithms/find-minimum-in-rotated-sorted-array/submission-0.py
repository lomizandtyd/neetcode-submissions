class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        """
        3 4 5 1 2
        4 5 1 2 3
        """

        while l < r:
            mid = l + (r -l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid           

        return nums[l]