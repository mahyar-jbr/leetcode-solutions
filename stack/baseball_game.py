# 682. Baseball Game
# Time: O(n) | Space: O(n)
# Stack of scores. Every op acts on the most recent scores (LIFO):
# int pushes, 'C' pops, 'D' doubles top, '+' sums top two. Return total.

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        listStack = []

        for char in operations:
            if char == '+':
                listStack.append(listStack[-1] + listStack[-2])
            elif char == 'C':
                listStack.pop()
            elif char == 'D':
                listStack.append(listStack[-1] * 2)
            else:
                listStack.append(int(char))

        return sum(listStack)