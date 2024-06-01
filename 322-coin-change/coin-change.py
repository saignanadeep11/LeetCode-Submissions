class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        ans=n+1
        self.dp=collections.defaultdict(int)
        def find(idx,n,k,steps):
            if(k in self.dp):
                return self.dp[k]
            if(k==0):
                return 0
            self.dp[k]=100000
            for i in range(n):
                # print(idx,k,steps,self.dp)
                if k-coins[i]>=0:
                    self.dp[k]=min(self.dp[k],find(i,n,k-coins[i],steps+1)+1)
            return self.dp[k]
        ans=find(0,n,amount,0)
        return ans if ans!=100000 else -1