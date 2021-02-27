# Definition for singly-linked list.
from typing import List
import heapq as hq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        return str(self.val) + ' -> ' + str(self.next)

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        hq.heapify(lists, lambda n1, n2: n1.val < n2.val)
        previous, head = None, None
        while lists:
            current = hq.heappop(lists)
            if current.next:
                hq.heappush(lists, current.next)
            if not previous:
                head = current
            else:
                previous.next = current
            previous = current
        return head


if __name__ == '__main__':
    lists = [ListNode(val=2, next=ListNode(val=4)), ListNode(val=1, next=ListNode(val=3)), ListNode(val=3, next=ListNode(val=4))]
    res = Solution().mergeKLists(lists)
    print(res)