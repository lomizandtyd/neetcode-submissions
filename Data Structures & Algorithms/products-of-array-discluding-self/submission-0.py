class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        a1 = [1] * len(nums)
        a2 = [1] * len(nums)

        for i in range(1, len(nums)):
            a1[i] = a1[i-1] * nums[i-1]

        for j in range(len(nums) - 2, -1, -1):
            a2[j] = a2[j+1] * nums[j+1]

        for i in range(0, len(nums)):
            a1[i] = a1[i] * a2[i]
        
        return a1