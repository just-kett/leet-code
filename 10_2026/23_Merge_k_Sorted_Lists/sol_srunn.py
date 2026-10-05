# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        if all(head is None for head in lists):
            return None
        kq=[]
        for head in lists:
            while head != None:
                kq.append(head.val)
                head = head.next
        kq.sort()
        head = ListNode(kq[0])
        tail = head
        for i in range(1,len(kq)):
            x = ListNode(kq[i])
            tail.next = x
            tail = tail.next
        return head