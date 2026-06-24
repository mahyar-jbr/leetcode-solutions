# 344. Reverse String
# Time: O(n) | Space: O(1)
# Two pointers from both ends, swap and converge toward the middle.
# In place, no extra array.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1