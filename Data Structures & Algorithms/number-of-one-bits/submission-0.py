class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0

        while n:
            i += n % 2
            n = n // 2

        return i