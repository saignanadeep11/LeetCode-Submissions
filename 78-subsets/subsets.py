class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        arrLen=pow(2,n)
        for i in range(arrLen):
            sarr=[]
            for j in range(32):
                if ((i)&(1<<j)):
                    sarr.append(nums[j])
            ans.append(sarr)
        return ans