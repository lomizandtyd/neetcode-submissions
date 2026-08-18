class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maxa = 0
        while i < j:

            a = min(heights[i], heights[j]) * (j-i)
            maxa = max(a, maxa)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1


        return maxa