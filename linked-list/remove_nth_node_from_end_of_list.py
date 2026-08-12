# 19. Remove Nth Node From End of List
# Time: O(n) | Space: O(1)
# One pass with two pointers separated by a gap of n, both starting at a
# dummy node so removing the head needs no special case. Advance fast n
# steps, then move both until fast is on the last node — slow is then the
# predecessor of the target, so splice it out.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next