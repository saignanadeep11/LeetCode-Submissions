class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        ans=0
        idx=nums[0]
        for i in range(1,n):
            # print(nums[i],idx)
            idx+=1
            if nums[i]<idx:
                ans+=abs(idx-nums[i])
            else:
                idx=nums[i]
        return ans