class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=[]
        d=defaultdict(int)
        for i in s1.split(" "):
            d[i]+=1
        for i in s2.split(" "):
            d[i]+=1
        for v in d:
            if d[v]==1:
                ans.append(v)
        return ans