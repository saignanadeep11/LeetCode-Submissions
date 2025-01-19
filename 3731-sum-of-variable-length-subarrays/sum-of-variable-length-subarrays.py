class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pre=[0,nums[0]]
        n=len(nums)
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])
        ans=0
        # print(pre)
        for i in range(n):
            k=max(0,i-nums[i])
            ans+=pre[i+1]-pre[k]
            # print(k,ans)
        return ans