class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        count=0
        z=s.count('0')
        if z==n or z==0:
            return n-1
        ans=0
        count1=0
        for i in range(n-1):
            if s[i]=='0':
                count+=1
            else:
                count1+=1
            ans=max(ans,count+abs(n-z-count1))
        return ans