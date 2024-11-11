class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minA=100000
        ans=0
        for i in prices:
            minA=min(minA,i)
            ans=max(ans,i-minA)
        return ans