class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        # print(n,m)
        for i in range(n):
            if(grid[i][0]==0):
                for j in range(m):
                    if grid[i][j]==1:
                        grid[i][j]=0
                    else:
                        grid[i][j]=1
        # print(grid)
        for i in range(m):
            count=0
            for j in range(n):
                if grid[j][i]==0:
                    count+=1
            # print(grid[j][i],j,i)
            # print(count,j,i)
            if(count>=n/2):
                for j in range(n):
                    if grid[j][i]==1:
                        grid[j][i]=0
                    else:
                        grid[j][i]=1
            ans=0
            for i in grid:
                ans+=int("".join(map(str,i)),2)
            # print(ans)
            # print(grid)
        return ans
  