class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            cursum = numbers[i] + numbers[j]
            if cursum == target:
                return [i+1, j+1]
            

            if j > i+1 and (numbers[i] + numbers[j-1]) >= target:
                j -= 1
            else:
                i+=1
        return [i+1, j+1]
