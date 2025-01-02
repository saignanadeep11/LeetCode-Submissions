# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur=head
        temp=cur
        half=head.next
        h=True
        halfHead=half
        while(cur):
            if h:
                half=cur.next
                h=False
            else:
                half.next=cur.next
                half=half.next
            if cur.next and cur.next.next:
                cur.next=cur.next.next
                cur=cur.next
            else:
                break
                # half.next=None
                # half=half.next
                # half.next=None
                # cur.next=halfHead
                # print("hi",temp,halfHead)
            # print(temp,"mid",half)
        if half:
            half.next=None
        cur.next=halfHead
        return temp
        


        