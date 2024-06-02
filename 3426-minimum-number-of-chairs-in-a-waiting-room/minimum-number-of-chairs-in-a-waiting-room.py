class Solution:
    def minimumChairs(self, s: str) -> int:
        ans=0
        re=0
        for i in s:
            if i=="E":
                ans+=1
            else:
                ans-=1
            re=max(ans,re)
        return re