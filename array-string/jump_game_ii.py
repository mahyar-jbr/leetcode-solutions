# 45. Jump Game II
# Time: O(n) | Space: O(1)
# Greedy: BFS-like approach with jump ranges

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_end = 0  
        farthest = 0    
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps