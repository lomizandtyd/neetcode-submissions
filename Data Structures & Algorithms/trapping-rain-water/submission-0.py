class Solution:
    def trap(self, height: List[int]) -> int:
        a1 = [0] * (len(height)+2)
        a2 = [0] * (len(height)+2)

        for i in range(1, len(height)):
            a1[i+1] = max(a1[i-1+1], height[i-1])

        for i in range(len(height) - 2, -1, -1):
            a2[i +1] = max(a2[i+1+1], height[i+1])


        k = 0

        for i in range(0, len(height)):
            subk = (min(a2[i+1],a1[i+1]) - height[i])
            if subk > 0:
                k += subk
            # print(i, k)

        return k