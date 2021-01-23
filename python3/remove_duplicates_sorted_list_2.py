# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        else:
            return str(self.val) + ' -> ' + str(self.next)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        previous, cursor, non_dup_prev, running_num, duplicate = head, head.next, None, head.val, False
        while cursor:
            if cursor.val == running_num:
                duplicate = True
            elif duplicate:
                duplicate = False
            else:
                duplicate = False
                if non_dup_prev:
                    non_dup_prev.next = previous
                    non_dup_prev = previous
                else:
                    head = previous
                    non_dup_prev = previous
            running_num = cursor.val
            previous = cursor
            cursor = cursor.next
        if non_dup_prev:
            if duplicate:
                non_dup_prev.next = None
            else:
                non_dup_prev.next = previous
        else:
            if duplicate:
                head = None
            else:
                head = previous
        return head


if __name__ == '__main__':
    l6 = ListNode(val=5)
    l5 = ListNode(val=5, next=l6)
    l4 = ListNode(val=3, next=l5)
    l3 = ListNode(val=3, next=l4)
    l2 = ListNode(val=2, next=l3)
    l1 = ListNode(val=1, next=l2)

    print(l1)
    sol = Solution().deleteDuplicates(l1)
    print(sol)