class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        d[0]=1
        n=len(nums)
        pre=nums[0]%k
        d[pre]+=1
        ans=0
        for i in range(1,n):
            pre+=nums[i]
            pre%=k
            d[pre]+=1
        # print(d)
        for key in (d):
            # print(key)
            val=d[key]
            ans+=val*(val-1)//2
        return ans