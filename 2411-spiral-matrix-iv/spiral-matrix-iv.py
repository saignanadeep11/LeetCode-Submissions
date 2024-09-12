# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat=[[-1]*n for i in range(m)]
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        curDir=0
        i=j=0
        while(head):
            # print(i,j,m,n,curDir)
            mat[i][j]=head.val
            if(i+dir[curDir][0]>=m or j+dir[curDir][1]>=n or i+dir[curDir][0]<0 or j+dir[curDir][1]<0 or mat[i+dir[curDir][0]][j+dir[curDir][1]]!=-1):
                curDir=(curDir+1)%4
            i+=dir[curDir][0]
            j+=dir[curDir][1]
            head=head.next
        return mat
