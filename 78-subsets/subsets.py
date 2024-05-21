class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def recursive(nums,idx,small,n):
            if(idx>=n):
                ans.append(small[:])
                return
            small+=[nums[idx]]
            recursive(nums,idx+1,small,n)
            small.pop()
            recursive(nums,idx+1,small,n)
            
        recursive(nums,0,[],len(nums))
        return ans