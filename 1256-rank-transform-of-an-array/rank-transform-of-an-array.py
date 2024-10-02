class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d=defaultdict(int)
        idx=0
        for i in set(arr):
            d[i]=idx
            idx+=1
        idx=0
        for i in sorted(d.keys()):
            d[i]=idx
            idx+=1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]+1
        return arr