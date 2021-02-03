# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        dp = dict()

        def generate_bst(start: int, end: int) -> List[TreeNode]:
            if (start, end) in dp:
                return dp[(start, end)]
            if start > end:
                return [None]
            if start == end:
                result = [TreeNode(val=start)]
                dp[(start, end)] = result
                return result

            result = list()
            for rt in range(start, end+1):
                left = generate_bst(start, rt-1)
                right = generate_bst(rt+1, end)
                for l in left:
                    for r in right:
                        node = TreeNode(val=rt, left=l, right=r)
                        result.append(node)
            dp[(start, end)] = result
            return result
        return generate_bst(1, n)


if __name__ == '__main__':
    Solution().generateTrees(3)