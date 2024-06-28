class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cou=[[0,0] for _ in range(n)]
        for u,v in roads:
            cou[u][0]=u
            cou[u][1]+=1
            cou[v][0]=v
            cou[v][1]+=1
        cou.sort(key=lambda k:k[1])
        ans=[0]*n
        i=1
        for u,v in cou:
            ans[u]=i
            i+=1
        result=0
        for u,v in roads:
            result+=ans[u]
            result+=ans[v]
        # print(cou)
        return result