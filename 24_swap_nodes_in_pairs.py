# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = head
        q = head.next
        new_head = head.next
        while True:
            p.next = q.next
            q.next = p
            temp = p
            p = q
            q = temp
            pre_p = q
            if p.next.next and q.next and q.next.next:
                p = p.next.next
                q = q.next.next
                pre_p.next = q
            else:
                break
        return new_head
