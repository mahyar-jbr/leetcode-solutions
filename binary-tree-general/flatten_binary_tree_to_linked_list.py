# 114. Flatten Binary Tree to Linked List
# Time: O(n) | Space: O(n) for the node list
# The flattened order is preorder. Collect nodes in preorder into a list,
# then link each node's right to the next node and set every left to None.
# O(1) space follow-up: walk down .right; at each node with a left child,
# attach its right subtree to the rightmost node of its left subtree, then
# move the left subtree to the right and clear left.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []

        def preorder(node):
            if node is None:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(nodes)):
            if i < len(nodes) - 1:
                nodes[i].right = nodes[i + 1]
            else:
                nodes[i].right = None
            nodes[i].left = None