from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = Counter(list(s))
        st = Counter(list(t))

        return sc == st