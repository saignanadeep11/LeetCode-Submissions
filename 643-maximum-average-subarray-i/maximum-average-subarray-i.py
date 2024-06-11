class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        cur= sum(nums[:k])
        m=cur
        for i in range(k,n):
            cur+=nums[i]
            cur-=nums[i-k]
            if cur>m:
                m=cur
            # m=max(m,cur)
        return m/k