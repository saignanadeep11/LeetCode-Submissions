class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def find(nums):
            nums=[str(i) for i in nums]
            nums.sort(key=lambda key:key*10,reverse=True)
            if(nums[0]=='0'):return '0'
            return "".join(nums)
        return find(nums)