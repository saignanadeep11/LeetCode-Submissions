class Solution:
    def maxSatisfaction(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        n=len(nums)
        ans=-1
        sum=0
        for i in range(n):
            sum=0
            id=0
            for j in range(i-1,n):
                sum+=nums[j]*id
                ans=max(ans,sum)
                id+=1
                # print(nums[j],sum,ans)
        return ans