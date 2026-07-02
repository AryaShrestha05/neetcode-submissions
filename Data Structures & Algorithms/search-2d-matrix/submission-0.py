class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1

        while i <= j:
            mid = (i + j) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return target in matrix[mid]
            elif target > matrix[mid][-1]:
                i = mid + 1
            else:
                j = mid - 1

        return False