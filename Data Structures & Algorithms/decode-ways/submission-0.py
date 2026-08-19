class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cnt = [0] * len(s)

        if not s or s[0] == "0":
            return 0

        cnt[0] = 1

        for i in range(1, n):

            if s[i] != '0':
                cnt[i] = cnt[i-1]

            if i > 0 and ((s[i] == '0' and s[i-1] in '12') or
                          (s[i] in "789" and s[i-1] == "1") or
                          (s[i] in "123456" and s[i-1] in "12")
            ):
                cnt[i] += (cnt[i-2] if i > 1 else 1)
            #print(cnt)

        return cnt[-1]


            