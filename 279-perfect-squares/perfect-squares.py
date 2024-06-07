class Solution:
    def numSquares(self, n: int) -> int:

        per=[i*i for i in range(1,int(sqrt(n))+1)]
        m=len(per)
        ans=[float('inf') for _ in range(n+1)]
        ans[0]=0
        for i in range(1,n+1):
            for j in per:
                if j>i:
                    break
                ans[i]=min(ans[i],ans[i-j]+1)
        return ans[-1]
        