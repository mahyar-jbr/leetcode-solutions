# 274. H-Index
# Time: O(n log n) | Space: O(1)
# Sort descending, find first position that doesn't satisfy h-index

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        
        return len(citations)