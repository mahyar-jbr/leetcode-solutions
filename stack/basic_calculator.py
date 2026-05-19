# 224. Basic Calculator
# Time: O(n) | Space: O(n)
# Single-pass char scan. Track result, number, sign.
# On '(' push (result, sign) and reset; on ')' commit number then
# combine with outer context via result*outer_sign + outer_result.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        number = 0
        sign = 1

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == '+' or char == '-':
                result = result + sign * number
                sign = 1 if char == '+' else -1
                number = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result = result + sign * number
                result = result * stack.pop() + stack.pop()
                sign = 1
                number = 0
            else:
                continue

        result += sign * number
        return result