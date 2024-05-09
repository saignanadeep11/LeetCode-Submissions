class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans=0
        for i in range(k):
            temp=happiness[i]-i
            if(temp>0):
                ans+=temp
            else:
                break
        return ans