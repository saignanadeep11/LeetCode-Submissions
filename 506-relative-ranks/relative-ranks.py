class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        ind=dict()
        for i in range(n):
            ind[score[i]]=i
        score.sort(reverse=True)
        ans=[0]*n
        if n>2:
            ans[ind[score[0]]]="Gold Medal"
            ans[ind[score[1]]]="Silver Medal"
            ans[ind[score[2]]]="Bronze Medal"
        if n>1:
            ans[ind[score[0]]]="Gold Medal"
            ans[ind[score[1]]]="Silver Medal"
            
        if n==1:
            ans[ind[score[0]]]="Gold Medal"
        for i in range(3,n):
            ans[ind[score[i]]]=str(i+1)
        return ans