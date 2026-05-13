# 155. Min Stack
# Time: O(1) for all operations | Space: O(n)
# Use two stacks: main stack for values, min_stack tracks min at each level.
# On push, append min(val, current_min) to min_stack so top is always current min.

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack:
            new_min = val
        else:
            new_min = min(val, self.min_stack[-1])
        self.min_stack.append(new_min)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]