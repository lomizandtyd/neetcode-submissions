class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                p2 = stack.pop(-1)
                p1 = stack.pop(-1)

                if t == '+':
                    res = p1 + p2
                elif t == '-':
                    res = p1 - p2
                elif t == '*':
                    res = p1 * p2
                else: # /
                    res = int(float(p1) / p2) if p2 != 0 else 0

                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]