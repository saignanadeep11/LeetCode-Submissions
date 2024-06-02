class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        mem=collections.defaultdict(int)
        def rec(k,idx):
            # print(k,idx)
            if(idx>=n):
                return 0
            if(mem[idx]):
                return mem[idx]
            mem[idx]=1000000000
            # for i in range(n):
            mem[idx]=min(cost[idx]+rec(k,idx+1),cost[idx]+rec(k,idx+2))
            # print(k,idx,mem,"pp")
            return mem[idx]
        rec(0,0)
        # print(mem)
        return min(mem[0],mem[1])