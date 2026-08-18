class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        l = 0 
        r = 0
        n = len(nums)

        ret = []

        while r+k <= n:
            q = list(nums[r:r+k])
            heapq.heapify_max(q)
            ret.append(q[0])
            r += 1

        return ret
