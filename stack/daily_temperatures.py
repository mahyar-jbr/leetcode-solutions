# 739. Daily Temperatures
# Time: O(n) | Space: O(n)
# Monotonic decreasing stack of indices. For each day, pop all colder
# days waiting on the stack and record their distance to this warmer day.
# Each index pushed once, popped at most once -> O(n).

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)

        return result