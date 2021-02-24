# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        copied_nodes = {}
        cursor = head
        previous = None
        new_head = None
        while cursor:
            copied = Node(x=cursor.val)
            if not previous:
                new_head = copied
            else:
                previous.next = copied
            previous = copied
            copied_nodes[cursor] = copied
            cursor = cursor.next
        c1, c2 = head, new_head
        while c1:
            if c1.random:
                c2.random = copied_nodes[c1.random]
            c1 = c1.next
            c2 = c2.next
        return new_head