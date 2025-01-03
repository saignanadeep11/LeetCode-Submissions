# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, A: ListNode, B: ListNode) -> Optional[ListNode]:
        a=set()
        while A:
            a.add(A)
            A=A.next
        while B:
            k=B
            if k in a:
                return k
            B=B.next
        return None