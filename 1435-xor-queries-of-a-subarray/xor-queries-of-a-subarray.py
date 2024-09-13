class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        for i in range(1,n):
            arr[i]=arr[i-1]^arr[i]
        res=[]
        m=len(queries)
        for i in range(m):
            if(queries[i][0]==0):
                res.append(arr[queries[i][1]])
            else:
                k=queries[i][0]-1
                k1=queries[i][1]
                ans=arr[k]^arr[k1]
                res.append(ans)
        return res