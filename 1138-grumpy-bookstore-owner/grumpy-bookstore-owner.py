class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans=0
        rans=0
        com=list(zip(customers,grumpy))
        # print(com,com[0][0],com[0][1])
        n=len(com)
        for i in range(n):
            if com[i][1]==0:
                ans+=com[i][0]
        for i in range(minutes):
            if com[i][1]==1:
                ans+=com[i][0]
        rans=ans
        # print(rans)
        idx=0
        for i in range(minutes,n):
            # print(rans,ans)
            if com[i][1]==1:
                ans+=com[i][0]
            if com[idx][1]==1:
                ans-=com[idx][0]
            idx+=1
            rans=max(ans,rans)
        return rans