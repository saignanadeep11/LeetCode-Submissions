# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ans=[-1,-1]
        arr=[]
        temp=head
        pre=temp.val
        temp=temp.next
        idx=1
        while temp:
            if not temp.next:
                break
            print(temp.val,pre,temp.next.val)
            if temp.val>pre and temp.next.val<temp.val:
                arr.append(idx)
            if temp.val<pre and temp.next.val>temp.val:
                arr.append(idx)
            pre=temp.val
            temp=temp.next
            idx+=1
        # print(arr)
        if len(arr)<2:return ans
        mi=1000000000
        for i in range(1,len(arr)):
            mi=min(mi,arr[i]-arr[i-1])
        ans[0]=mi
        ans[1]=arr[len(arr)-1]-arr[0]
        return ans