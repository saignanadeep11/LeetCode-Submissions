class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=s[0]
        count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                count=1
            if(count<=2):
                ans+=s[i]

        return ans