class Solution:
    def equalSubstring(self, s: str, p: str, maxCost: int) -> int:
        ans=0
        start=0
        n=len(s)
        cur=0
        for i in range(n):
            cur+=abs(ord(s[i])-ord(p[i]))
            while(cur>maxCost):
                cur-=abs(ord(s[start])-ord(p[start]))
                start+=1
            ans=max(ans,i-start+1)
        return ans