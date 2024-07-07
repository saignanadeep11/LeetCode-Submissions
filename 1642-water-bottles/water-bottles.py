class Solution:
    def numWaterBottles(self, n: int, m: int) -> int:
        ans=0
        ans+=n
        while(n>=m):
            ans+=n//m
            n=(n%m)+(n//m)
            # print(ans,n)
        return ans
        