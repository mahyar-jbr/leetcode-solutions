# 20. Valid Parentheses
# Time: O(n) | Space: O(n)
# Stack-based matching: push opens, pop and verify on close.
# Closing bracket must match the most recently opened (LIFO).

class Solution(object):
    def isValid(self, s):
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack