# 3. Longest Substring Without Repeating Characters
# Time: O(n) | Space: O(min(n, m))
# Sliding window + dictionary to track last seen index

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        maxLength = 0
        char_index = {}

        for right in range(len(s)):
            char = s[right]
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength