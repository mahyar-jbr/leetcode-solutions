# 28. Find the Index of the First Occurrence in a String
# Time: O(n * m) | Space: O(1)
# Check each starting position with substring matching

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1