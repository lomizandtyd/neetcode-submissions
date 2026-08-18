class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = [[]] * (len(nums)+1)

        cnt = Counter(nums)
        return [kk for kk, v in cnt.most_common(k)]