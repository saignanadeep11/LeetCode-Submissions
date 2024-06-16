class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count=[0]*24
        ans=0
        for i in hours:
            ans+=count[(24-i%24)%24]
            count[i%24]+=1
        return ans