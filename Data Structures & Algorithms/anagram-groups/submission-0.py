from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = dict()
        for s in strs:
            sk = tuple(sorted(list(s)))
            
            if sk not in ret:
                ret[sk] = [s]

            else:
                ret[sk].append(s)

        return list(ret.values())


