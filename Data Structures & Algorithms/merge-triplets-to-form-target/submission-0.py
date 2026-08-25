class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        finda = findb = findc = False
        for (a, b, c) in triplets:
            if a == target[0] and b <= target[1] and c <= target[2]:
                finda = True
            if a <= target[0] and b == target[1] and c <= target[2]:
                findb = True
            if a <= target[0] and b <= target[1] and c == target[2]:
                findc = True

        return finda and findb and findc