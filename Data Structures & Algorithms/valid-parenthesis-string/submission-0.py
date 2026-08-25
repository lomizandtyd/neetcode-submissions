class Solution:
    def checkValidString(self, s: str) -> bool:
        s1, s2 = [], []

        for cid, c in enumerate(s):
            if c == '(':
                s1.append(cid)
            elif c == '*':
                s2.append(cid)
            else: # if c == ")"
                if len(s1) > 0:
                    s1 = s1[:-1]
                elif len(s2) > 0:
                    s2 = s2[:-1]
                else:
                    return False

        if len(s1) == 0:
            return True

        #
        if len(s1) > len(s2):
            return False

        for cidl, cids in zip(s1[::-1], s2[::-1]):
            if cidl > cids:
                return False
        return True