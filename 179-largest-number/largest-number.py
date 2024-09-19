class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(i) for i in nums]
        nums.sort(key=lambda k:(k*10),reverse=True)
        if(nums[0]=='0'): return '0'
        return "".join(nums)