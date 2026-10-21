# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Time: O(n^2) worst case (index lookup + slicing per call) | Space: O(n^2) slices
# postorder[-1] is the root. Its position mid in inorder splits the values:
# inorder[:mid] is left, inorder[mid+1:] is right. Postorder is laid out as
# [left][right][root], so left = postorder[:mid], right = postorder[mid:-1].
# O(n) version: value->index dict + index bounds instead of slices.

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)

        inorderLeft = inorder[:mid]
        inorderRight = inorder[mid + 1:]
        postorderLeft = postorder[:mid]
        postorderRight = postorder[mid:-1]

        root.left = self.buildTree(inorderLeft, postorderLeft)
        root.right = self.buildTree(inorderRight, postorderRight)

        return root