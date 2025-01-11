class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=defaultdict(list)
        for i in range(n):
            p1=i+1
            p2=n-1
            while(p1<p2):
                k=nums[i]+nums[p1]+nums[p2]
                if(k)==0:
                    arr=str(nums[i])+str(nums[p1])+str(nums[p2])
                    if arr not in ans:
                        ans[arr]=[nums[i],nums[p1],nums[p2]]
                    p1+=1
                    p2-=1
                elif k>0:
                    p2-=1
                else:
                    p1+=1
        return(list(ans.values()))
        