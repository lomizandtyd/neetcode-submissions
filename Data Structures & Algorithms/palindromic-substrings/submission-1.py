class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        def mancher(s):
            t = "#" + "#".join(s) + "#"
            n = len(t)
            p = [0] * n
            l, r = 0, 0

            for i in range(n):
                #
                p[i] = min(r - i, p[l + r - i]) if i < r else 0

                #
                while (i+p[i]+1) < n and (i - p[i] - 1) >= 0 and t[i+p[i]+1] == t[i-p[i]-1]:
                    p[i] += 1

                #
                if i+p[i] > r:
                    l = i - p[i] - 1
                    r = p[i]

            cnt = 0
            for i in p:
                cnt += (i+1) // 2
            return cnt
        return mancher(s)

        for i in range(len(s)):
            cnt += 1

            # even
            l,r = i, i+1
            
            while l>=0 and r <len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

            # odd
            l, r = i-1, i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

        return cnt