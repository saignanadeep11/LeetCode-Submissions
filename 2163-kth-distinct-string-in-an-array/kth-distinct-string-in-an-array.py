class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dist=defaultdict(int)
        for i in arr:
            dist[i]+=1
        idx=0
        for i in dist:
            if dist[i]==1:
                idx+=1
            if idx==k:
                return i
        return ""
