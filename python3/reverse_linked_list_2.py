# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return str(self.val) + ' -> ' + str(self.next)
        return str(self.val)


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or m >= n:
            return head

        def reverse_list(h: ListNode) -> ListNode:
            if not h or not h.next:
                return h
            nxt = h.next
            h.next = None
            new_head = reverse_list(nxt)
            nxt.next = h
            return new_head

        m_1_node, m_node, n_node, n_1_node = None, None, None, None
        cursor, pos = head, 1
        if m == 1:
            m_node = head
        while cursor:
            if pos == m-1:
                m_1_node, m_node = cursor, cursor.next
            elif pos == n:
                n_node, n_1_node = cursor, cursor.next
                break
            cursor = cursor.next
            pos = pos+1

        if not m_node or not n_node:
            return head

        n_node.next = None
        rlist = reverse_list(m_node)
        if m_1_node:
            m_1_node.next = rlist
        else:
            head = rlist
        m_node.next = n_1_node

        return head


if __name__ == '__main__':
    l4 = ListNode(val=4)
    l3 = ListNode(val=3, next=l4)
    l2 = ListNode(val=2, next=l3)
    l1 = ListNode(val=1, next=l2)
    print(l1)
    print(Solution().reverseBetween(l1, 1, 4))