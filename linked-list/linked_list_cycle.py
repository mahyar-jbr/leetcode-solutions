# 141. Linked List Cycle
# Time: O(n) | Space: O(1)
# Floyd's Tortoise and Hare: slow moves 1 step, fast moves 2.
# If they meet, cycle exists. If fast hits None, no cycle.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False