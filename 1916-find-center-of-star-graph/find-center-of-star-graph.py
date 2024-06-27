class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic=defaultdict(list)
        for k,v in edges:
            dic[k].append(v)
            dic[v].append(k)
        # print(dic,n)
        n=len(dic)
        for k in dic:
            # print(len(dic[k]),k)
            if len(dic[k])==n-1:
                return k
        return 1