class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        q = [[]]
        total = set()

        for n in sorted(nums):
            nq = q.copy()
            for ss in q:
                ssc = ss.copy()
                nq.append(ssc + [n])

            q = nq

        for ss in q:
            total.add(tuple(ss))

        return [list(ss) for ss in total]