# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def check(self,st,k):
        if(len(st)==0):
            st.append(k)
            return st
        temp=st.pop()
        if(temp.val>=k.val):
            st.append(temp)
            st.append(k)
        else:
            st=self.check(st,k)
        return st
    def removeNodes(self, head):
        st=[]
        while(head!=None):
            k=head
            if(len(st)>0):
                temp=st.pop()
                if temp.val>=k.val:
                    st.append(temp)
                    st.append(k)
                else:
                    st=self.check(st,k)
            else:
                st.append(k)
            head=head.next

        for i in range(len(st)-1):
            st[i].next=st[i+1]
        return st[0]
    