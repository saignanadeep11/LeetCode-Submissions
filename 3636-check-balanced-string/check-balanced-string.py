class Solution:
    def isBalanced(self, nums: str) -> bool:
        n=0
        for i in range(len(nums)):
            if(i%2==0):
                n+=int(nums[i])
            else:
                n-=int(nums[i])
        if n==0:
            return True
        return False