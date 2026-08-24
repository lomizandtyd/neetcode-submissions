
"""
0 1 2 3 4 5 6  7  8 9 10 11 12 13
4 0 4 0 4 0 4  0  4 0  4  0  4  0
4 0 6 0 8 0 10 0 12 0 14  0 16  0
0
        8
                 12
                            16 
                                 

"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        maxs, newmaxs = nums[0], nums[0]
        cnt = 1
        i = 0

        for i in range(len(nums) - 1):
            newmaxs = max(newmaxs, i + nums[i])

            if i == maxs:
                maxs = newmaxs
                cnt += 1

        return cnt
        