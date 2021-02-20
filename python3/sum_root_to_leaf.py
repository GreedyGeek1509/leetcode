# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        total_sum = 0

        def back_track(node: TreeNode, num_so_far: int):
            nonlocal total_sum
            if not node:
                return
            num = 10*num_so_far + node.val
            if not node.left and not node.right:
                total_sum += num
                return
            back_track(node.left, num)
            back_track(node.right, num)

        back_track(root, 0)
        return total_sum