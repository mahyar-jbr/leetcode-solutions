# 100. Same Tree
# Time: O(n) | Space: O(h) recursion stack
# Recurse on both trees in lockstep. Both None -> match; one None -> shapes
# differ. Otherwise values must match AND left pairs AND right pairs must
# match. Value check goes first so a mismatch short-circuits the recursion.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        equal = p.val == q.val

        return equal and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)