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
        return a + b
        res = 0
        car = 0
        # i = 0
        for i in range(32):
            abit, bbit = a&1, b&1
            rem = (abit ^ bbit) ^ car
            car = (abit & bbit) | ((abit ^ bbit) & car)

            if rem:
                res = res | (rem << i)
            a = a >> 1
            b = b >> 1
            print(i, res, rem, car, abit, bbit)
            # i = i << 1 if i & 1 else i | 1

        res = res | (car << i)
        mask = 0xFFFFFFFF
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res
