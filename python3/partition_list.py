# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head

        last_node, prev = None, None
        cursor = head
        while cursor:
            if cursor.val < x:
                if prev:
                    prev.next = cursor.next
                if last_node:
                    tmp = last_node.next
                    last_node.next = cursor
                    cursor.next = tmp
                    last_node = cursor
                else:
                    if cursor != head:
                        cursor.next = head
                        head = cursor
                    last_node = cursor
            prev = cursor
            cursor = cursor.next
        return head
