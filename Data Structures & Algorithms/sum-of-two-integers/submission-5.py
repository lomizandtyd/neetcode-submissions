class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
bitsum
01010101
10110101

abit, bbit = a^1, b^1
rem = (abit ^ bbit) ^ car
car = (abit & bbit) | (abit ^ bbit & car)

        """
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b:
            car = (a & b) << 1
            a = (a ^ b) & mask
            b = car & mask

        return a if a <= max_int else ~(a ^ mask)
