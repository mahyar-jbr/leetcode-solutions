# 76. Minimum Window Substring
# Time: O(n) | Space: O(m)
# Sliding window: expand to find valid, shrink to find minimum

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        required = len(t_count)
        formed = 0
        window_count = {}
        left = 0
        min_len = len(s) + 1
        min_start = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                
                left += 1

        if min_len == len(s) + 1:
            return ""
        return s[min_start : min_start + min_len]