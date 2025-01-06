class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        preMax=[]
        sufMax=[0]*n
        for i in height:
            if preMax:
                preMax.append(max(preMax[-1],i))
            else:
                preMax.append(i)
        for i in range(n-1,-1,-1):
            if i==n-1:
                sufMax[i]=height[i]
                continue
            sufMax[i]=max(sufMax[i+1],height[i])
        ans=0
        for i in range(n):
            ans+=abs(min(sufMax[i],preMax[i])-height[i])
        return ans