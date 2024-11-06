class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        count={}
        n=len(nums)
        for i in set(nums):
            c=0
            for j in range(32):
                if (i>>j)&1==1:
                    c+=1
            count[i]=c
        temp=nums[:]
        for i in range(n):
            for j in range(n-1):
                if i==j:
                    continue
                if count[nums[j+1]]!=count[nums[j]]:
                    continue
                if nums[j]>nums[j+1]:
                    t=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=t
        
        
        temp.sort()
        return temp==nums