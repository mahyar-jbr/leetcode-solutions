# 92. Reverse Linked List II
# Time: O(n) | Space: O(1)
# Dummy node removes the left==1 special case. Walk to the node before
# position left, then run the three-pointer reversal exactly
# (right - left + 1) times. After the loop prev is the reversed head and
# current is the node past the sublist, so reconnect both boundaries.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        before = dummy
        for i in range(left - 1):
            before = before.next

        sublist_head = before.next
        prev = None
        current = sublist_head
        for i in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        before.next = prev
        sublist_head.next = current

        return dummy.next