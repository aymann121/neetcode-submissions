class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)*len(matrix[0]) -1

        while l <= r:
            m = (r + l) // 2
            v = matrix[m // len(matrix[0])][m % len(matrix[0])]
            if v > target:
                r = m-1
            elif v < target:
                l = m+1
            else:
                return True
        return False
