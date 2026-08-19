"""
[1,2,3]

[[1,2],[2,1]] * [3]

[] 1
[1] 2
[1, 2], [2, 1] 3


"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        q = [[]]

        i = 0
        for n in nums:
            nq = []
            for subs in q:
                for idx in range(i+1):
                    scopy = subs.copy()
                    scopy.insert(idx, n)
                    nq.append(scopy)
            i += 1
            q = nq
        return q



