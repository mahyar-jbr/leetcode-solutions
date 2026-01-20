# 15. 3Sum
# Time: O(n²) | Space: O(1)
# Sort + two pointers for each element, skip duplicates

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for outer in range(len(nums) - 2):
            if outer > 0 and nums[outer] == nums[outer - 1]:
                continue
            
            left = outer + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[outer] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[outer], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result