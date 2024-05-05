class Solution:
    def maxSatisfaction(self, nums: List[int]) -> int:
        nums.sort()
        ans=cnt=0
        while nums:
            cur=nums.pop()
            if cur+cnt<0:
                return ans
            cnt+=cur
            ans+=cnt
        return ans