# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        ans=ListNode(0)
        ret=ans
        while(l1 and l2):
            sum=l1.val+l2.val+c
            c=sum//10
            ans.next=ListNode(sum%10)
            ans=ans.next
            l1=l1.next
            l2=l2.next

        while(l1):
            sum=l1.val+c
            c=sum//10
            ans.next=ListNode(sum%10)
            ans=ans.next
            l1=l1.next
        while(l2):
            sum=l2.val+c
            c=sum//10
            ans.next=ListNode(sum%10)
            ans=ans.next
            l2=l2.next
        if c:
            ans.next=ListNode(c)
        return ret.next