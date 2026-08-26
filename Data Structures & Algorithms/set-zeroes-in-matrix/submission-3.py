class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rid, cid = set(), set()


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rid.add(i)
                    cid.add(j)

        for i in range(m):
            for j in range(n):
                if i in rid or j in cid:
                    matrix[i][j] = 0

        