# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ans=head
        pre=None
        m=max(nums)
        fre=[0]*(m+1)
        # print(fre)
        for i in nums:
            fre[i]=1
        while(head):
            # print(head.val,1)
            if(head.val<=m and fre[head.val]==1):
                if head.next:
                    head.val=head.next.val
                    head.next=head.next.next
                else:
                    # print(pre.val,head.val,3)
                    pre.next=None
                    head=None
            else:
                pre=head
                head=head.next
        return ans
        