# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        a=head
        b=a.next
        ans=b
        if not b:
            return a
        if not b.next:
            b.next=a
            a.next=None
            return b
        c=b.next
        if not c.next:
            b.next=a
            a.next=c
            return b
        while c:
            b.next=a
            b=c
            c=c.next
            if c:
                a.next=c
            else:
                a.next=b
            a=b
            b=c
            if c:
                c=c.next 
        if b:
            b.next=a
            a.next=None
        return ans