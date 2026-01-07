# 42. Trapping Rain Water
# Time: O(n) | Space: O(1)
# Two pointers: track left_max and right_max

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        result = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                result += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                result += rMax - height[r]
        
        return result