# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flatten_helper(node: TreeNode) -> (TreeNode, TreeNode):
            if not node or (not node.left and not node.right):
                return node, node
            left_root, left_leaf = flatten_helper(node.left)
            right_root, right_leaf = flatten_helper(node.right)
            node.left = None
            if left_root:
                node.right = left_root
                left_leaf.right = right_root
            if not right_leaf:
                right_leaf = left_leaf
            return node, right_leaf

        flatten_helper(root)