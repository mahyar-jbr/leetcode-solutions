# 26. Remove Duplicates from Sorted Array
# Time: O(n) | Space: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        write = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[write-1]:
                nums[write] = nums[i]
                write += 1
        return write