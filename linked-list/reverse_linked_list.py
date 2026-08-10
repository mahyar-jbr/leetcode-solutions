# 206. Reverse Linked List
# Time: O(n) | Space: O(1)
# Three-pointer in-place reversal. Per node, in this exact order:
# save next, flip current.next to prev, advance prev, advance current.
# Loop ends when current is None; prev is the new head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev