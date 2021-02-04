# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node: TreeNode, lft, rt) -> bool:
            if not node:
                return True
            if node.val <= lft or node.val >= rt:
                return False

            return valid(node.left, lft, node.val) and valid(node.right, node.val, rt)

        return valid(root, float('-inf'), float('inf'))

    def isValidBST2(self, root: TreeNode) -> bool:
        def inorder_traverse(top: TreeNode) -> List[int]:
            if not top:
                return []
            left = inorder_traverse(top.left)
            left.append(top.val)
            right = inorder_traverse(top.right)
            return left+right

        io = inorder_traverse(TreeNode)
        length = len(io)
        for i in range(1, length):
            if io[i] <= io[i-1]:
                return False
        return True
