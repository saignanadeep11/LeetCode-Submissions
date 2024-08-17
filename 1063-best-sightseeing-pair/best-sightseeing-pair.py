class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        mn=0
        smin=0
        for i in values:
            mn=max(mn,smin+i)
            smin=max(smin,i)-1
        return mn