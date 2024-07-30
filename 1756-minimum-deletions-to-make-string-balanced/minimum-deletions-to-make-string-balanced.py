class Solution:
    def minimumDeletions(self, s: str) -> int:
        n=len(s)
        cal=[[0,0] for _ in range(n)]
        m=0
        for i in range(n):
            cal[i][0]=m
            if s[i]=='b':
                m+=1
        m=0
        for i in range(n-1,-1,-1):
            cal[i][1]=m
            if s[i]=='a':
                m+=1
        # print(cal)
        ans=sys.maxsize
        for i in range(n):
            ans=min(ans,cal[i][0]+cal[i][1])
        return ans