class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red=nums.count(0)
        wh=nums.count(1)
        bl=nums.count(2)
        idx=0
        while(red):
            nums[idx]=0
            idx+=1
            red-=1
        while(wh):
            nums[idx]=1
            idx+=1
            wh-=1
        while(bl):
            nums[idx]=2
            idx+=1
            bl-=1