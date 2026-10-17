# 226. Invert Binary Tree
# Time: O(n) | Space: O(h) recursion stack
# Each node swaps its own left and right children; recursion mirrors
# everything below. Empty tree inverts to None. Changes the tree in place
# and returns the root.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root