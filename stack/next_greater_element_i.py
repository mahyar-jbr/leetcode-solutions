# 496. Next Greater Element I
# Time: O(n + m) | Space: O(n)
# Monotonic decreasing stack over nums2 builds a {value: next_greater} map.
# When a bigger number resolves stack tops, record the mapping.
# Then look up each nums1 value, defaulting to -1.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                greater[stack[-1]] = num
                stack.pop()
            stack.append(num)

        return [greater.get(n, -1) for n in nums1]