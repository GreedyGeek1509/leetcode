# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            length = len(queue)
            first = queue.pop(0)
            if first.left:
                queue.append(first.left)
            if first.right:
                queue.append(first.right)
            for i in range(length-1):
                second = queue.pop(0)
                if second.left:
                    queue.append(second.left)
                if second.right:
                    queue.append(second.right)
                first.next = second
                first = second
        return root