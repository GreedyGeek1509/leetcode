# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        result: ListNode = None
        previous: ListNode = None
        carry: int = 0
        while l1 or l2 or carry != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sm = v1+v2+carry
            current: ListNode = ListNode(val=sm % 10)
            if previous:
                previous.next = current
            else:
                result = current
            previous = current
            carry = sm//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result
