class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        c = 1

        for i in range(len(digits)):
            c, digits[i] = divmod(digits[i]+c, 10)

        if c:
            digits.append(c)

        digits.reverse()

        return digits
            