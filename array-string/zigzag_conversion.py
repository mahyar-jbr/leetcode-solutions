# 6. Zigzag Conversion
# Time: O(n) | Space: O(n)
# Track current row and direction, flip at edges

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        result = [""] * numRows
        currentRow = 0
        goingDown = False

        for char in s:
            result[currentRow] += char
            
            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown
            
            if goingDown:
                currentRow += 1
            else:
                currentRow -= 1

        return "".join(result)