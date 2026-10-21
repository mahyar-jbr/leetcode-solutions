# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Time: O(n^2) worst case (index lookup + slicing per call) | Space: O(n^2) slices
# preorder[0] is the root. Its position mid in inorder splits the values:
# inorder[:mid] is the left subtree, inorder[mid+1:] the right. mid is also
# the left subtree's size, so preorder[1:mid+1] is left, preorder[mid+1:] right.
# Recurse on matching slices. O(n) version: value->index dict + index bounds.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root