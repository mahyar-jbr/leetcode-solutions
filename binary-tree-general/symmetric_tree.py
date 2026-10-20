# 101. Symmetric Tree
# Time: O(n) | Space: O(h) recursion stack
# Symmetric means the left subtree mirrors the right subtree. Helper walks
# two nodes at once (like Same Tree) but compares crossed pairs: outer
# (a.left, b.right) and inner (a.right, b.left). Values must match too.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isMirror(root.left, root.right)

    def isMirror(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False

        return a.val == b.val and self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)