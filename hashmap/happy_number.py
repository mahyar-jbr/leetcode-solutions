# 202. Happy Number
# Time: O(log n) | Space: O(log n)
# Sum of squares of digits, detect loop with set

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.get_sum(n)

        return True

    def get_sum(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n = n // 10
        return total