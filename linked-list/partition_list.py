# 86. Partition List
# Time: O(n) | Space: O(1)
# Two chains built with two dummy heads: nodes < x and nodes >= x.
# Splice existing nodes in one pass, so relative order is preserved.
# Cut the big chain's tail (its last node still points at an old
# neighbor and would form a cycle), then attach small tail to big head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy_small = ListNode(0) # type: ignore
        dummy_big = ListNode(0) # type: ignore
        small = dummy_small
        big = dummy_big
        current = head

        while current:
            if current.val < x:
                small.next = current
                small = small.next
            else:
                big.next = current
                big = big.next
            current = current.next

        big.next = None
        small.next = dummy_big.next
        return dummy_small.next