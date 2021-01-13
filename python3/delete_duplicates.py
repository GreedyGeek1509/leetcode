# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        value = head.val
        prev = head
        cursor = head.next
        while cursor:
            if value == cursor.val:
                cursor = cursor.next
                prev.next = cursor
            else:
                value = cursor.val
                prev = cursor
                cursor = cursor.next
        return head
