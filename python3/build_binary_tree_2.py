from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        length = len(inorder)

        def build_tree(istart: int, iend: int, pstart: int, pend: int) -> TreeNode:
            if istart < 0 or istart > iend or iend >= length or pstart < 0 or pstart > pend or pend >= length:
                return None
            root_val = postorder[pend]
            iroot_idx = inorder.index(root_val)
            left_length = iroot_idx - istart
            left_tree = build_tree(istart, iroot_idx-1, pstart, pstart+left_length-1)
            right_tree = build_tree(iroot_idx+1, iend, pstart+left_length, pend-1)
            return TreeNode(val=root_val, left=left_tree, right=right_tree)

        return build_tree(0, length-1, 0, length-1)