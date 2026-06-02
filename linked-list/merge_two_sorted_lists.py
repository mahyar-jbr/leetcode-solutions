# 21. Merge Two Sorted Lists
# Time: O(n + m) | Space: O(1)
# Dummy head + current pointer. At each step, splice the smaller node.
# When one list ends, bulk-attach the remainder of the other.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy

        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val <= current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        current.next = current1 if current1 else current2
        return dummy.next