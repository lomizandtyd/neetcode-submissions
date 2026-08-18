class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mins, minl = "", 1e10

        l = 0

        tmap = Counter(t)
        cmap = tmap.copy()

        def findall(cmap):
            for v in cmap.values():
                if v > 0:
                    return False
            return True

        while l < len(s) and s[l] not in tmap:
            l += 1

        r = l
        while l < len(s):
            # find a match
            while r < len(s) and not findall(cmap):
                if s[r] in cmap:
                    cmap[s[r]] -= 1
                r += 1

            #
            if (r-l) < minl and findall(cmap):
                minl = r - l
                mins = s[l:r]

            # print(l, r, mins)
            # advance
            if l < len(s) and s[l] in cmap:
                cmap[s[l]] += 1
            l += 1

            # skip 
            while l < r and (s[l] not in cmap or cmap[s[l]] < 0):
                if s[l] in cmap:
                    cmap[s[l]] += 1
                l += 1
            # print("- ", l, r, s[l:r], s[l] in cmap if l < len(s) else -1)

        return mins