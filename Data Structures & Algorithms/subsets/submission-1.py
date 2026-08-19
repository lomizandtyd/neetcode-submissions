class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        q = res

        for n in nums:
            nq = q.copy()
            for pq in q:
                nq.append(pq + [n])

            q = nq

        return q
