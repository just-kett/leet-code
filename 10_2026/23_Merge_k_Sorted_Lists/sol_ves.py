# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        min_heap = []
        for l in lists:
            curr = l
            while curr:
                heapq.heappush(min_heap, curr.val)
                curr = curr.next
        res = ListNode(0)
        tail = dummy
        while min_heap:
            val = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next
        return res.next