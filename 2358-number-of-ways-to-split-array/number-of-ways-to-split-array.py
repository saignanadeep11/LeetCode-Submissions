class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[nums[0]]
        suf=[0]*n
        suf[-1]=nums[-1]
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])
        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]+nums[i]
        ans=0
        for i in range(n-1):
            if pre[i]>=suf[i+1]:
                ans+=1
        return ans