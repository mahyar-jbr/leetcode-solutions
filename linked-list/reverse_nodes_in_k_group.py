# 25. Reverse Nodes in k-Group
# Time: O(n) | Space: O(1)
# Dummy node so the first group needs no special case. Per group:
# walk k steps to confirm k nodes remain (if not, return and leave the
# rest as-is), run the three-pointer reversal exactly k times, reconnect
# before.next = prev and sublist_head.next = current, then advance
# before to sublist_head, which is now the group's tail.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        before = dummy

        while True:
            node = before.next
            for i in range(k):
                if not node:
                    return dummy.next
                node = node.next

            sublist_head = before.next
            prev = None
            current = sublist_head
            for i in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            before.next = prev
            sublist_head.next = current

            before = sublist_head