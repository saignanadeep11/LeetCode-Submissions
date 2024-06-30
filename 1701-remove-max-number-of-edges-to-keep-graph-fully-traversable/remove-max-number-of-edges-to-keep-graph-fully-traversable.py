class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class df:
            def __init__(self,n):
                self.n=n
                self.parents=[i for i in range(n+1)]
                self.edges=0
            def find(self,x):
                if x!=self.parents[x]:
                    self.parents[x]=self.find(self.parents[x])
                return self.parents[x]
            def union(self,x,y):
                if self.find(x)==self.find(y):
                    return False
                self.parents[self.find(x)]=self.find(y)
                self.edges+=1
                return True
        alice=df(n)
        bob=df(n)
        countEdges=0
        notNes=0
        for t,u,v in edges:
            if t==3:
                if (alice.union(u,v) |
                bob.union(u,v)):
                    countEdges+=1
                else:
                    notNes+=1
                
        for t,u,v in edges:
            if t==1:
                if alice.union(u,v):
                    countEdges+=1
                else:
                    notNes+=1
            elif t==2 :
                if bob.union(u,v):
                    countEdges+=1
                else:
                    notNes+=1
        # print(countEdges,notNes,alice.edges,bob.edges)
        if alice.edges<n-1 or bob.edges<n-1:
            return -1
        return notNes