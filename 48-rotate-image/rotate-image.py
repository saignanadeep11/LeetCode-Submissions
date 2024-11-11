class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n-1):
            for j in range(n-1-i*2):
                pre=[[i,j+i],[j+i,n-1-i],[n-1-i,n-1-j-i],[n-1-j-i,i]]
                temp=-10000
                for k in range(5):
                    cur=pre[k%4]
                    if temp==-10000:
                        temp=matrix[cur[0]][cur[1]]
                    else:
                        temp2=matrix[cur[0]][cur[1]]
                        matrix[cur[0]][cur[1]]=temp
                        temp=temp2
                print(pre)


        """
        Do not return anything, modify matrix in-place instead.
        """
        