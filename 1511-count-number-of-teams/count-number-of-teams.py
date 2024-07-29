class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        inc=[[0]*4 for i in range(n)]
        dec=[[0]*4 for i in range(n)]
        for i in range(n):
            inc[i][1]=1
            dec[i][1]=1
        for i in range(2,4):
            for j in range(n):
                for k in range(j+1,n):
                    if rating[k]>rating[j]:
                        inc[k][i]+=inc[j][i-1]
                    # print(i,rating[j],rating[k])
                    # print(inc)
        for i in range(2,4):
            for j in range(n):
                for k in range(j+1,n):
                    if rating[k]<rating[j]:
                        dec[k][i]+=dec[j][i-1]
        ans=0
        # print(inc,dec)
        for i in range(n):
            ans+= inc[i][3]
            ans+=dec[i][3]
        return ans