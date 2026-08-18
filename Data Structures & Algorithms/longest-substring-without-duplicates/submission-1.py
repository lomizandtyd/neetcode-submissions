class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        maxl = 1

        if len(s) < 2:
            return len(s)

        while l < len(s) and r < len(s):
            isDup = False
            for j in range(l, r):
                if s[r] == s[j]:
                    isDup = True
                    maxl = max(maxl, r-l)
                    l = j+1
                    break
            r += 1

        return max(maxl, r-l)
            