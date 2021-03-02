class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKNodes(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 2:
            return head

        def reverse_nodes(node: ListNode, position: int) -> (ListNode, ListNode, ListNode):
            if not node:
                return None, None, None
            if position == 1:
                return node, node, node.next


        new_head = None
        cursor, h, tail, next_cursor = head, None, None, None
        while cursor:
            counter = k

