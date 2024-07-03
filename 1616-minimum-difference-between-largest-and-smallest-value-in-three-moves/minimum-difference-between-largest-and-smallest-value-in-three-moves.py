class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        n=len(nums)
        if n<=4:
            return 0
        ans=sys.maxsize
        p1=0
        p2=n-4
        while(p2<n and p1<n):
            ans=min(abs(nums[p1]-nums[p2]),ans)
            p1+=1
            p2+=1
        return ans