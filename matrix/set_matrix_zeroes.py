# 73. Set Matrix Zeroes
# Time: O(m * n) | Space: O(m + n)
# Two passes: find zeroes, then set rows and cols to zero

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0