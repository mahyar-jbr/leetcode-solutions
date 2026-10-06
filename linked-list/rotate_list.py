# 61. Rotate List
# Time: O(n) | Space: O(1)
# First pass finds the length and old tail. k %= length (rotating by the
# length is a no-op). Walk length - k - 1 steps to the new tail, then:
# old tail -> old head, save the node after new tail as the new head,
# and cut the new tail's link.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or head.next is None:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k = k % length
        if k == 0:
            return head

        steps = length - k - 1
        new_tail = head
        for i in range(steps):
            new_tail = new_tail.next

        tail.next = head
        head = new_tail.next
        new_tail.next = None

        return head