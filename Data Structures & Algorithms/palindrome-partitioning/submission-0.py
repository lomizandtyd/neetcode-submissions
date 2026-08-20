class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        mem = {}

        def isPalindrome(s):
            if len(s) == 1:
                return True

            l, r = 0, len(s) - 1

            while l <= r:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            return True


        def dfs(l, path):
            nonlocal res, mem, s
            if l >= len(s):
                return

            for k in range(l+1, len(s)+1):
                if s[l:] in mem:
                    res.append([s[l:k]] + mem[s[l:]])
                elif isPalindrome(s[l:k]):
                    path.append(s[l:k])
                    if k == len(s):
                        res.append(path.copy())
                    dfs(k, path)
                    path.pop(-1)
        dfs(0, [])
        return res