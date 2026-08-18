class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)

        for tidx, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                ptidx, _ = stack.pop(-1)
                res[ptidx] = tidx - ptidx

            stack.append((tidx, t))

        return res