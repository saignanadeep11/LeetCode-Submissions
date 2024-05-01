class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        n=len(nums)
        print(n,nums)
        for i in range(0,n,3):
            l=[]
            if(nums[i+2]-nums[i]<=k):
                l.append(nums[i])
                l.append(nums[i+1])
                l.append(nums[i+2])
            else:
                return []
            ans.append(l)
        return ans