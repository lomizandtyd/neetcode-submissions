class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # binary search r id first.

        l = 0
        r = m
        rid = m

        while l < r:
            mid = (l + r - 1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
                if mid+1 == m or (mid+1 < m and matrix[mid+1][0] > target):
                    rid = mid
                    break
            else:
                r = mid
        # print(rid)
        if rid >= m:
            return False

        l = 0
        r = n

        while l < r:
            mid = (l + r - 1) // 2
            if matrix[rid][mid] == target:
                return True
            elif matrix[rid][mid] < target:
                l = mid + 1
            else:
                r = mid

        return False