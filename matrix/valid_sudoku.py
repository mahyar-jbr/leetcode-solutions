# 36. Valid Sudoku
# Time: O(81) = O(1) | Space: O(81) = O(1)
# Use sets to track seen numbers in rows, cols, and boxes

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == '.':
                    continue
                
                if num in rows[row]:
                    return False

                if num in cols[col]:
                    return False

                box_id = (row // 3) * 3 + (col // 3)
                if num in boxes[box_id]:
                    return False
                
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_id].add(num)
        
        return True