class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []

        for s in strs:
            ret.append(str(len(s)))
            ret.append('#')
            ret.append(s)
        
        return ''.join(ret)

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0

        while i < len(s):
            idx = s.find('#', i)

            length = int(s[i:idx])
            i = idx + 1
            subs = s[i:i+length]
            i = idx + 1 + length
            ret.append(subs)
        
        return ret
