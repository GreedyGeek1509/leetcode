from typing import List


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []

        def back_track(node: TreeNode, sum_so_far: int, path_so_far: List[int]):
            if not node.left and not node.right:
                if sum_so_far == targetSum:
                    res.append(list(path_so_far))
                return
            if node.left:
                path_so_far.append(node.left.val)
                back_track(node.left, sum_so_far+node.left.val, path_so_far)
                path_so_far.pop()
            if node.right:
                path_so_far.append(node.right.val)
                back_track(node.right, sum_so_far+node.right.val, path_so_far)
                path_so_far.pop()

        back_track(root, root.val, [root.val])
        return res