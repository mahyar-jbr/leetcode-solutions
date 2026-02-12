# 1. Two Sum
# Time: O(n) | Space: O(n)
# Store seen numbers, check if complement exists

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in seen:
                return [seen[remain], i]
            seen[num] = i