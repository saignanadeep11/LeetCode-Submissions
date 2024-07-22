class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        com=list(zip(heights,names))
        com.sort(reverse=True)
        ans=[]
        for h,n in com:
            ans.append(n)
        return ans