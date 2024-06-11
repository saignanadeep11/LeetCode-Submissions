class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d=defaultdict(int)
        for i in arr1:
            d[i]+=1
        # print(sorted(d),d)
        ans=[]
        for i in arr2:
            ans+=[i]*d[i]
            d[i]=0
        for i in sorted(d):
            if d[i]>0:
                ans+=[i]*d[i]
        return ans