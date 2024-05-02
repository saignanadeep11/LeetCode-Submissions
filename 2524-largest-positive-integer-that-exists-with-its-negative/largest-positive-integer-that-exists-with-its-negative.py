class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for i in range(n-1,-1,-1):
            k=nums[i]*-1
            if k in nums:
                return nums[i]
        return -1