class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        breakP=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                breakP=i
                break
        if breakP==-1:
            nums.reverse()
        else:
            for i in range(n-1,breakP,-1):
                if nums[i]>nums[breakP]:
                    t=nums[i]
                    nums[i]=nums[breakP]
                    nums[breakP]=t
                    nums[breakP+1:]=reversed(nums[breakP+1:])
                    break
        """
        Do not return anything, modify nums in-place instead.
        """
        