# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs_with_queue(tr: TreeNode) -> List[List[int]]:
            r = []
            if not tr:
                return r
            queue = [tr]
            while len(queue) > 0:
                length = len(queue)
                level_list = list()
                for i in range(length):
                    popped = queue.pop(0)
                    level_list.append(popped.val)
                    if popped.left:
                        queue.append(popped.left)
                    if popped.right:
                        queue.append(popped.right)
                r.append(level_list)
            return r
        return bfs_with_queue(root)