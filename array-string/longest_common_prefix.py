# 14. Longest Common Prefix
# Time: O(n * m) where n = number of strings, m = shortest string length
# Space: O(1)
# Compare character by character across all strings

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        shortest_len = min(len(s) for s in strs)
        
        for i in range(shortest_len):
            char = strs[0][i]
            
            for s in strs:
                if char != s[i]:
                    return result
            
            result += char
        
        return result