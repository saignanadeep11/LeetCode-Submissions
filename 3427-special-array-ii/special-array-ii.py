class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n=len(nums)
        pre=[[0,0] for i in range(n)]
        val=0
        for i in range(n-1):
            if(nums[i]%2==nums[i+1]%2):
                val+=1
            pre[i][1]=val
            pre[i+1][0]=val
        ans=[]
        # print(pre)
        for s,e in queries:
            ans.append(pre[s][0]==pre[e][0])
        return ans