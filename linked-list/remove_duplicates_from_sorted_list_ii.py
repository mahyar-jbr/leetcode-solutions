# 82. Remove Duplicates from Sorted List II
# Time: O(n) | Space: O(1)
# Sorted input means duplicates are adjacent. prev tracks the last kept
# node (starts at a dummy so a duplicated head is handled); current scans.
# On a duplicate run, advance current to the run's last node and splice
# the whole run out with prev.next = current.next, leaving prev in place.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev = dummy

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next