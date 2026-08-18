class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []

        q = deque()

        l = 0 
        r = 0
        n = len(nums)

        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (l + k-1) == r:
                ret.append(nums[q[0]])
                l += 1
            r += 1

        return ret