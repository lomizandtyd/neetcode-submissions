class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        n = len(s)

        mmap = {s[0]: 1}
        
        maxl = 1

        if len(s) < 2:
            return len(s)

        while l < n:
            if k + max(mmap.values()) >= (r - l):
                maxl = max(maxl, r - l)
                if r < n:
                    mmap[s[r]] = mmap.get(s[r], 0) + 1
                    r += 1
                else:
                    mmap[s[l]] -= 1
                    l += 1
            else:
                mmap[s[l]] -= 1
                l += 1

        return maxl