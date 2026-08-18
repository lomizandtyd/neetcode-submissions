class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l = 0
        r = m*n

        while l < r:
            mid = (l + r - 1) // 2

            rid = mid // n
            cid = mid % n
            if matrix[rid][cid] == target:
                return True
            elif matrix[rid][cid] < target:
                l = mid + 1
            else:
                r = mid

        return False