# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        result = list()

        def level_traverse(tr: TreeNode, level: int):
            if not tr:
                return
            if level < len(result):
                result[level].append(tr.val)
            else:
                result.append([tr.val])

            level_traverse(tr.left, level+1)
            level_traverse(tr.right, level+1)

        level_traverse(root, 0)
        return result