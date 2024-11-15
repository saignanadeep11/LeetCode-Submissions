class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat=[[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i==0:
                    mat[i][j]=1
                elif j==0:
                    mat[i][j]=1
                else:
                    mat[i][j]=mat[i-1][j]+mat[i][j-1]
        return mat[m-1][n-1]