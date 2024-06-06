class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3: return 2
        if n==4: return 4
        if n==5: return 6
        ans=6
        idx=1
        p1=3
        for i in range(6,n+1):
            if idx==3:
                idx=1
                t=p1
                p1=p1*2
                ans+=p1
                p1+=t
            else:
                idx+=1
                ans+=p1
            # print(i,ans,p1)
        return ans