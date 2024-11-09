class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        col=1
        row=1
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                    if i==0:
                        col=0
                    if j ==0:
                        row=0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0]==0:
                    matrix[i][j]=0
                if matrix[0][j]==0:
                    matrix[i][j]=0
        if row==0:
            for i in range(n):
                matrix[i][0]=0
        if col==0:
            for i in range(m):
                matrix[0][i]=0        
            
        """
        Do not return anything, modify matrix in-place instead.
        """
        