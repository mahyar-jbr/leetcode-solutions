# 112. Path Sum
# Time: O(n) | Space: O(h) recursion stack
# Subtract each node's value from the target on the way down. Empty node:
# no path. A leaf is the only place the answer is decided: its value must
# equal the remaining target. Otherwise recurse into both children with the
# reduced target and OR the results (one valid path is enough).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)