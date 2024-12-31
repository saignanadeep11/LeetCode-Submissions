class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        lo=0
        hi=n-1
        while(lo<=hi):
            mid=(lo+hi)>>1
            if(nums[lo]<=nums[mid] and nums[mid]<=nums[hi]):
                hi=mid-1
            elif(nums[mid]<nums[hi]):
                hi=mid
            else:
                lo=mid+1
            # print(lo,mid,hi)
        return nums[lo]