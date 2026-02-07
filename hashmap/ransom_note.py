# 383. Ransom Note
# Time: O(m + n) | Space: O(k) where k = unique chars in magazine
# Count magazine letters, check if ransomNote can be made

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        magazineDict = {}
        for char in magazine:
            magazineDict[char] = magazineDict.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in magazineDict or magazineDict[char] == 0:
                return False
            magazineDict[char] -= 1
        
        return True