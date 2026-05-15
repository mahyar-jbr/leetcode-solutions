# 150. Evaluate Reverse Polish Notation
# Time: O(n) | Space: O(n)
# Stack-based postfix evaluation. Push numbers; on operator, pop b then a,
# apply operation, push result. Use int(a/b) for truncation toward zero.

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[-1]