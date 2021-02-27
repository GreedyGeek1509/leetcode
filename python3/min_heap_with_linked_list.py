# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LHeap:
    def __init__(self):
        self.heap = [ListNode(val=0, next=None)]
        self.size = 0

    def get_min_child(self, i: int):
        mc = 2*i
        if 2*i+1 <= self.size and self.heap[2*i+1].val < self.heap[2*i].val:
            mc = 2*i+1
        return mc

    def shift_up(self, i: int):
        while i//2 > 0:
            if self.heap[i].val < self.heap[i//2].val:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def shift_down(self, i: int):
        while 2*i <= self.size:
            mc = self.get_min_child(i)
            if self.heap[i].val > self.heap[mc].val:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def insert(self, node: ListNode):
        if node:
            self.heap.append(node)
            self.size += 1
            self.shift_up(self.size)

    def extract_min(self):
        mini = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop(self.size)
        self.size -= 1
        self.shift_down(1)
        return mini

    def empty(self):
        return self.size == 0

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        heap = LHeap()
        for node in lists:
            heap.insert(node)

        previous, head = None, None

        while not heap.empty():
            mini = heap.extract_min()
            heap.insert(mini.next)
            if previous:
                previous.next = mini
            else:
                head = mini
            previous = mini

        return head