# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        length = len(preorder)

        def build_tree(pstart: int, pend: int, istart: int, iend: int) -> TreeNode:
            if pstart < 0 or pstart > pend or pend >= length or istart < 0 or istart > iend or iend >= length:
                return None

            root_val = preorder[pstart]
            i_root_idx = inorder.index(root_val)
            left_length = i_root_idx - istart
            left_tree = build_tree(pstart+1, pstart+left_length, istart, i_root_idx-1)
            right_tree = build_tree(pstart+1+left_length, pend, i_root_idx+1, iend)
            return TreeNode(val=root_val, left=left_tree, right=right_tree)

        return build_tree(0, length-1, 0, length-1)