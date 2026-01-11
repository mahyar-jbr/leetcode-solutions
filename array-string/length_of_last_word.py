# 58. Length of Last Word
# Time: O(n) | Space: O(n)
# Use split() to get words and return length of last one

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])