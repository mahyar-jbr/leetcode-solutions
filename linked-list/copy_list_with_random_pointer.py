# 138. Copy List with Random Pointer
# Time: O(n) | Space: O(n)
# Two passes with an {original: copy} map.
# Pass 1 creates every copy node; pass 2 wires next/random via the map,
# so a random pointer to a not-yet-visited node still resolves.
# Seeding the map with {None: None} removes all null special-casing.

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        mapping = {None: None}

        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            mapping[current].next = mapping[current.next]
            mapping[current].random = mapping[current.random]
            current = current.next

        return mapping[head]