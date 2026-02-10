# 242. Valid Anagram
# Time: O(n) | Space: O(k) where k = unique chars
# Count chars in s, verify t has same counts

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char not in s_dict:
                return False
            elif s_dict[char] == 0:
                return False
            s_dict[char] -= 1
        
        return True