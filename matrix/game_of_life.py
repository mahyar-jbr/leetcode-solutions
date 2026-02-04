# 289. Game of Life
# Time: O(m * n) | Space: O(m * n)
# Copy board, count neighbors from copy, apply rules to original

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        copy = [[board[i][j] for j in range(cols)] for i in range(rows)]

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for i in range(rows):
            for j in range(cols):
                count = 0
                for dr, dc in directions:
                    nr = i + dr
                    nc = j + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        count += copy[nr][nc]

                if copy[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                else:
                    if count == 3:
                        board[i][j] = 1