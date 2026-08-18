class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(list(s1))

        ak = len(s1)
        for i in range(0, len(s2) - ak+1):
            if Counter(s2[i:i+ak]) == c1:
                return True

        return False