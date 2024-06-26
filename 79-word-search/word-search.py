class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n=len(board)
        m=len(board[0])
        wordlen=len(word)
        def dp(i,j,k,flag):
            # print(i,j,k)
            if(k>=wordlen):
                return True
            if(i<0 or j<0 or i>=n or j>=m or flag[i][j]==-1):
                return False
            
            if(board[i][j]==word[k]):
                flag[i][j]=-1
                ans=(dp(i-1,j,k+1,flag)or dp(i+1,j,k+1,flag)or dp(i,j-1,k+1,flag)or dp(i,j+1,k+1,flag) )
                flag[i][j]=0
                return ans
            return False
        for i in range(n):
            for j in range(m):
                
                if board[i][j]==word[0]:
                    flag=[[0 for i in range(m)] for i in range(n)]
                    if(dp(i,j,0,flag)):
                        return True
        return False