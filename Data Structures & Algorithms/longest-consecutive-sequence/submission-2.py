class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mmap = {}
        if len(nums) == 0:
            return 0
            
        maxv = 1
        for n in nums:
            mmap[n] = 1

        for n in nums:
            if n-1 not in mmap:
                while n+1 in mmap:
                    mmap[n+1] = mmap[n] + 1
                    maxv = max(maxv, mmap[n+1])
                    n += 1
        return maxv

        