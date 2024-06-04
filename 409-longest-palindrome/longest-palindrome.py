class Solution:
    def longestPalindrome(self, s: str) -> int:
        flag=[0]*60
        n=len(s)
        m=0
        def check(flag):
            c=0
            ans=0
            for i in flag:
                if(i%2!=0):
                    c+=1
                    ans+=i-1
                else:
                    ans+=i
            return ans+1 if c>0 else ans
        for i in range(n):
            flag[ord(s[i])-65]+=1
            m=max(m,check(flag))
        return m