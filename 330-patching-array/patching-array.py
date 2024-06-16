class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        l=len(nums)
        i=0
        ans=0
        m=1
        while(m<=n):
            if i<l and nums[i]<=m:
                m+=nums[i]
                i+=1
            else:
                m+=m
                # i+=1
                ans+=1
        return ans