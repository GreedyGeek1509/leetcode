from typing import List


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        while len(queue) > 0:
            length = len(queue)
            sublist = list()
            for i in range(length):
                popped = queue.pop(0)
                sublist.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            res.insert(0, sublist)
        return res
