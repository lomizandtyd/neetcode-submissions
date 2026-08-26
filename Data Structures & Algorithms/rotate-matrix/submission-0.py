class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.flip(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(0, n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def flip(self, matrix):
        n = len(matrix)

        for i in range(0, n):
            matrix[i].reverse()