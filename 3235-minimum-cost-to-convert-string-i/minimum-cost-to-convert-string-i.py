class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        min_cost=[[float('inf')]*26 for _ in range(26)]
        for s,t,c in list(zip(original,changed,cost)):
            min_cost[ord(s)-ord('a')][ord(t)-ord('a')]=min(min_cost[ord(s)-ord('a')][ord(t)-ord('a')],c)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j]=min(min_cost[i][j],min_cost[i][k]+min_cost[k][j])
        result=0
        for s,t in zip(source,target):
            if s==t:
                continue
            if min_cost[ord(s)-ord('a')][ord(t)-ord('a')]==float('inf'):
                return -1
            result+=min_cost[ord(s)-ord('a')][ord(t)-ord('a')]
        return result