class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans=0
        n=len(arrays)
        low=arrays[0][0]
        high=arrays[0][-1]
        for i in range(1,n):
            ans=max(ans,abs(arrays[i][0]-high),abs(arrays[i][-1]-low))
            low=min(low,arrays[i][0])
            high=max(high,arrays[i][-1])
        return ans