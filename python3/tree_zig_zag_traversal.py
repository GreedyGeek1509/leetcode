# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        flip = True
        while len(queue) > 0:
            length = len(queue)
            sublist = list()
            for i in range(length):
                popped = queue.pop(0)
                if flip:
                    sublist.insert(0, popped.val)
                else:
                    sublist.append(popped.val)
                ln, rn = popped.left, popped.right
                if ln:
                    queue.append(ln)
                if rn:
                    queue.append(rn)
            res.append(sublist)
            flip = not flip
        return res