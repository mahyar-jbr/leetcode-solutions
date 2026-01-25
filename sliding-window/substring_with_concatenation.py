# 30. Substring with Concatenation of All Words
# Time: O(n * m * k) | Space: O(m)
# Check each starting position, split into chunks, compare word counts

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        window_size = word_len * num_words
        result = []
        
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        for i in range(len(s) - window_size + 1):
            window = s[i : i + window_size]
            
            window_count = {}
            for j in range(num_words):
                start = j * word_len
                chunk = window[start : start + word_len]
                window_count[chunk] = window_count.get(chunk, 0) + 1
            
            if window_count == word_count:
                result.append(i)
        
        return result