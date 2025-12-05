# 88. Merge Sorted Array
# Time: O(m+n) | Space: O(1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        p = m + n - 1
        m = m - 1
        n = n - 1

        while n >= 0:
            if m < 0 or nums2[n] >= nums1[m]:
                nums1[p] = nums2[n]
                p -= 1
                n -= 1
            else:
                nums1[p] = nums1[m]
                p -= 1
                m -= 1