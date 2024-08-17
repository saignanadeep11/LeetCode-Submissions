class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=100000
        ans=0
        for i in prices:
            mn=min(mn,i)
            if mn<i:
                ans=max(ans,i-mn) 
                 
        return ans