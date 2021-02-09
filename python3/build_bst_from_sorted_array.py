from typing import List


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) < 1:
            return None
        length = len(nums)

        def build_bst(beg: int, end: int) -> TreeNode:
            if beg > end:
                return None
            root_idx = (beg+end)//2
            lft_tree = build_bst(beg, root_idx-1)
            rght_tree = build_bst(root_idx+1, end)
            return TreeNode(val=nums[root_idx], left=lft_tree, right=rght_tree)

        return build_bst(0, length-1)