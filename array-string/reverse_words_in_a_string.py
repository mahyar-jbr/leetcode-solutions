# 151. Reverse Words in a String
# Time: O(n) | Space: O(n)
# Split, reverse, join with space trimming

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = ""
        
        for word in words[-1::-1]:
            result = result + word + " "
        
        return result.strip()