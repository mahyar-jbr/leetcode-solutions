# 54. Spiral Matrix
# Time: O(m * n) | Space: O(1)
# Track 4 boundaries, traverse right/down/left/up, shrink inward

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        total = len(matrix) * len(matrix[0])
        count = 0

        result = []

        while count < total:
            for col in range(left, right + 1):
                if count < total:
                    result.append(matrix[top][col])
                    count += 1
            top += 1

            for row in range(top, bottom + 1):
                if count < total:
                    result.append(matrix[row][right])
                    count += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if count < total:
                        result.append(matrix[bottom][col])
                        count += 1
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if count < total:
                        result.append(matrix[row][left])
                        count += 1
                left += 1

        return result