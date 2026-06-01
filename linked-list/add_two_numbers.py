# 2. Add Two Numbers
# Time: O(max(n, m)) | Space: O(max(n, m))
# Walk both lists simultaneously, summing digits + carry.
# Use dummy head to simplify list construction.
# Loop while either list has nodes or carry remains.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy

        l1Current = l1
        l2Current = l2
        carry = 0

        while l1Current or l2Current or carry:
            val1 = l1Current.val if l1Current else 0
            val2 = l2Current.val if l2Current else 0
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            current.next = ListNode(digit)
            current = current.next
            if l1Current:
                l1Current = l1Current.next
            if l2Current:
                l2Current = l2Current.next

        return dummy.next