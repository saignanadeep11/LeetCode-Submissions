class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        t=heights[:]
        t.sort()
        ans=0
        for idx,v in enumerate(heights):
            if v!=t[idx]:
                ans+=1
        return ans