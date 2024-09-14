class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        an=nums[0]
        for i in range(1,n):
            if an==0:
                an=nums[i]
            else:
                an=an&nums[i]
                nums[i]=max(an,nums[i])
        m=max(nums)
        c=0
        ans=0
        for i in nums:
            if i==m:
                c+=1
                ans=max(c,ans)
            else:
                c=0
        return ans