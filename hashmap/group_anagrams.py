# 49. Group Anagrams
# Time: O(n * k log k) where k = max word length | Space: O(n)
# Use sorted word as key to group anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_dict = {}
        
        for word in strs:
            key = "".join(sorted(word))
            
            if key not in sorted_dict:
                sorted_dict[key] = []
            sorted_dict[key].append(word)
        
        return list(sorted_dict.values())