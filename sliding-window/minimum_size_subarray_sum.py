# 209. Minimum Size Subarray Sum
# Time: O(n) | Space: O(1)
# Sliding window: expand right, shrink left when sum >= target

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        currentSum = 0
        minLength = len(nums) + 1

        for right in range(len(nums)):
            currentSum += nums[right]
            
            while currentSum >= target:
                minLength = min(minLength, right - left + 1)
                currentSum -= nums[left]
                left += 1

        return minLength if minLength != len(nums) + 1 else 0