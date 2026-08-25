class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret = []

        end = {}

        # record the last position
        for cid, c in enumerate(s):
            end[c] = cid


        prev = 0
        curend = 0
        for cid, c in enumerate(s):
            curend = max(curend, end[c])
            if cid == curend:
                ret.append(curend+1-prev)
                prev = curend + 1

        return ret

