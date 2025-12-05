# 80. Remove Duplicates from Sorted Array II
# Time: O(n) | Space: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        write = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[write-2]:
                nums[write] = nums[i]
                write += 1
        return write