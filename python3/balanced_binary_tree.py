class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height_and_balanced(node: TreeNode) -> (int, bool):
            if not node:
                return 0, True
            lft, rt = height_and_balanced(node.left), height_and_balanced(node.right)
            return 1 + max(lft[0], rt[0]), lft[1] and rt[1] and -1 <= lft[0] - rt[0] <= 1

        return height_and_balanced(root)[1]