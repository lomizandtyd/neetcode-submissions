class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        expect = {"{":"}", "[": "]", "(": ")"}
        expect_r = {v: k for k, v  in expect.items()}

        for c in s:
            if c in expect_r:
                if len(stack) == 0 or stack[-1] != expect_r[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0

