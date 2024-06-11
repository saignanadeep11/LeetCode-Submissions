class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        ans=p1=0
        while(p1<k):
            ans+=nums[p1]
            p1+=1
        p2=k
        p1=0
        m=ans/k
        # print(ans,m)
        while(p2<n and p2-p1==k):
            ans+=nums[p2]
            ans-=(nums[p1])
            p1+=1
            p2+=1
            m=max(m,(ans/k))
            # print(p1,p2,ans,m)
        return m