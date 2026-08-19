class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        # maintain a decreasing stack
        stack = []
        for hidx, h in enumerate(heights):
            if not stack:
                stack.append([hidx, h])
            else:
                start = hidx
                while stack and stack[-1][1] > h:
                    prevl, prevh = stack.pop(-1)
                    maxA = max(maxA, prevh * (hidx - prevl))
                    start = min(start, prevl)

                stack.append([start, h])


        for l, h in stack:
            maxA = max(maxA, h * (len(heights) - l))

        return maxA

            

    def largestRectangleArea2(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            heights.append(0)
            return max(heights)

        maxh = heights.copy()

        for i in range(len(heights)):
            minh = heights[i]
            for j in range(i+1, len(heights)):
                minh = min(minh, heights[j])
                maxh[i] = max(maxh[i], minh * (j-i+1))

        return max(maxh)
