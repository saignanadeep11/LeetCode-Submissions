# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        p1=head
        p2=head.next
        tail=None
        while(p2):
            t=p2.next
            p2.next=p1
            p1.next=tail
            tail=p1
            p1=p2
            p2=t
        return p1