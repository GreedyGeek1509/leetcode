# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        prev, cursor, double_runner = None, head, head.next.next if head.next else None
        while double_runner:
            prev = cursor
            cursor = cursor.next
            double_runner = double_runner.next.next if double_runner.next else None

        if prev:
            prev.next = None
        if cursor:
            left_head = head if prev else None
            right_head = cursor.next if cursor else None
            lft_tree = self.sortedListToBST(left_head)
            rgt_tree = self.sortedListToBST(right_head)
            return TreeNode(val=cursor.val, left=lft_tree, right=rgt_tree)
        else:
            return None