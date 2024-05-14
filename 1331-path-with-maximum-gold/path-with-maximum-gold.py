class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        # flag=[[0]*m]*n
        ans=-1
        def find(i,j,sum):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0:
                return sum
            # print(i,j,grid[i][j],sum)
            
            sum+=grid[i][j]
            temp=grid[i][j]
            grid[i][j]=0
            sum=max(find(i+1,j,sum),
            find(i-1,j,sum),
            find(i,j+1,sum),
            find(i,j-1,sum))
            grid[i][j]=temp
            return sum
    
        for i in range(n):
            # flag=[[0]*m]*n
            for j in range(m):
                ans=max(ans,find(i,j,0))
        return ans