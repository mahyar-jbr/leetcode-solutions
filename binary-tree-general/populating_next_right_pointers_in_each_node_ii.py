# 117. Populating Next Right Pointers in Each Node II
# Time: O(n) | Space: O(w) queue, w = widest level
# Level-order BFS. Record each level's size before popping so we know which
# nodes belong to it. Each node's next is the front of the queue, unless it
# is the last node in its level, where next stays None.

from collections import deque

# Definition for a Node.
# class Node(object):
#     def __init__(self, val=0, left=None, right=None, next=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None

        queue = deque([root])
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()

                if i < levelSize - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root