class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        n=len(s)
        for i in range(0,n-1):
            # print((chr)s[i])
            ans+=abs(ord(s[i])-ord(s[i+1]))
        return ans