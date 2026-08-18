class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        ret = []

        while i < j:
            cursum = numbers[i] + numbers[j]
            if cursum == target:
                ret.append([i, j])
                i += 1
                j -= 1
            elif cursum < target:
                i += 1
            else:
                j -= 1
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        ret2 = []
    
        for i in range(0, len(nums) - 2):

            rets = self.twoSum(nums[i+1:], -nums[i])
            # print(-nums[i], nums[i:], ret)
            if len(rets) > 0:
                for ret in rets:
                    ret2.append(
                        [nums[i], nums[i +1 + ret[0]], nums[i +1+ ret[1]]]
                    )

        ret2 = set(tuple(k) for k in ret2)
        return list(ret2)