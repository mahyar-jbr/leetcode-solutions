# 104. Maximum Depth of Binary Tree
# Time: O(n) | Space: O(h) recursion stack, h = tree height
# Recursive DFS. Base case: empty tree has depth 0.
# Each node's depth is 1 (itself) + the deeper of its two subtrees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        left = root.left
        right = root.right

        return 1 + max(self.maxDepth(left), self.maxDepth(right))