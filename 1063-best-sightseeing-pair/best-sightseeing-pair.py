class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans=0
        hi=values[0]
        for i in range(1,len(values)):
            ans=max(ans,hi+values[i]-i)
            hi=max(hi,values[i]+i)
        return ans