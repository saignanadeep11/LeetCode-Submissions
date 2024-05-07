# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num=0
        sys.set_int_max_str_digits(100000)
        while head!=None:
            k=head.val
            num=num*10+k
            head=head.next
        num=str(num*2)
        k=ListNode(int(num[0]))
        ans=k
        for i in range(1,len(num)):
            k.next=ListNode(num[i])
            k=k.next
        return ans
        