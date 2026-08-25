class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            b = n & 1
            res = res | (b << (31 - i))
            n = n >> 1

        return res
