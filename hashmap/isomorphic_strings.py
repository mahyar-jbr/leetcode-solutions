# 205. Isomorphic Strings
# Time: O(n) | Space: O(k) where k = unique chars
# Two hashmaps to check mapping in both directions

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            if (s[i] in s_to_t) and (s_to_t[s[i]] != t[i]):
                return False
            s_to_t[s[i]] = t[i]

            if (t[i] in t_to_s) and (t_to_s[t[i]] != s[i]):
                return False
            t_to_s[t[i]] = s[i]

        return True