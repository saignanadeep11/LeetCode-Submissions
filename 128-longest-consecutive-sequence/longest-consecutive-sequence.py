class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        # if not 
        t=set(nums)
        for i in t:
            y=i+1
            if i-1 not in t:
                while y in t:
                    y+=1
                ans=max(ans,y-i)
        return ans