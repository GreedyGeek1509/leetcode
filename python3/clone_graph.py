# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        cloned_nodes = {}
        queue = [node]
        while queue:
            length = len(queue)
            for i in range(length):
                popped = queue.pop(0)
                if popped.val not in cloned_nodes:
                    cloned_nodes[popped.val] = Node(val=popped.val)
                    for n in popped.neighbors:
                        queue.append(n)

        queue = [node]
        while queue:
            popped = queue.pop(0)
            if not cloned_nodes[popped.val].neighbors:
                cloned_nodes[popped.val].neighbors = [cloned_nodes[n.val] for n in popped.neighbors]
                for n in popped.neighbors:
                    queue.append(n)

        return cloned_nodes[node.val]

