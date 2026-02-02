# 48. Rotate Image
# Time: O(n²) | Space: O(1)
# Transpose matrix then reverse each row

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                copy = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = copy

        for row in matrix:
            row.reverse()