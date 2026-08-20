class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n2l = {
            "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz", "0": ""
        }

        if not digits:
            return []

        res = []


        q = [""]
        nq = []

        for d in digits:
            nq = []
            for seq in q:
                for l in n2l[d]:
                    # print(d, seq, l)
                    nq.append(seq+l)
            q = nq

        return q