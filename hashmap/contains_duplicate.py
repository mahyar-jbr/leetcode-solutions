# 217. Contains Duplicate
# Time: O(n) | Space: O(n)
# Track seen values in a set (O(1) membership). Return True on first repeat.
# Space-constrained alternative: sort, then check adjacent pairs (O(n log n), O(1)).

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set()
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                return True
        return False