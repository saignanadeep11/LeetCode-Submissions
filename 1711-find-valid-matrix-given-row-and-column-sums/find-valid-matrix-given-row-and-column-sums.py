class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n=len(colSum)
        m=len(rowSum)
        res=[[0]*n for j in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=res[i][j]
                colSum[j]-=res[i][j]
        return res