class Solution:
    def numWaterBottles(self, n: int, m: int) -> int:
        ans=n
        while(n>=m):
            ans+=n//m
            n=(n%m)+(n//m)
            # print(ans,n)
        return ans
        