# 290. Word Pattern
# Time: O(n) | Space: O(k) where k = unique chars/words
# Two hashmaps to check mapping in both directions

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        pattern_to_words = {}
        words_to_pattern = {}

        for i in range(len(words)):
            if (pattern[i] in pattern_to_words) and (pattern_to_words[pattern[i]] != words[i]):
                return False
            if (words[i] in words_to_pattern) and (words_to_pattern[words[i]] != pattern[i]):
                return False
            
            pattern_to_words[pattern[i]] = words[i]
            words_to_pattern[words[i]] = pattern[i]
        
        return True