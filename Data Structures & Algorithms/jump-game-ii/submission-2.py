class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_end = 0
        cnt = 0
        far = 0

        for i, n in enumerate(nums[:-1]):
            far = max(far, n+i)
            if cur_end == i:
                cnt += 1
                cur_end = max(cur_end, far)
        return cnt