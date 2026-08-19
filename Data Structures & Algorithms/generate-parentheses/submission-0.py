class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        tgt = n * 2

        q = [""]

        for i in range(tgt):
            nq = []
            for sq in q:
                nq.append(sq + "(")
                nq.append(sq + ")")
            q = nq

        nq = []

        def validpar(s):
            stack = []
            # print(" --", s)
            for c in s:
                # print(" --- ", c, stack)
                if c == "(":
                    stack.append(c)
                else:
                    if not stack:
                        return False
                    if not stack.pop(-1) != ")":
                        return False

            return len(stack) == 0

        for sq in q:
            if validpar(sq):
                nq.append(sq)
            # print(sq, validpar(sq))
        return nq

            