class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev(s):
            return s[::-1]
        def invert(s):
            for i in range(len(s)):
                s[i]='1' if s[i]=='0' else '0'
            return s
        ans=["0"]
        for i in range(n-1):
            m=[]
            small=rev(invert(ans[:]))
            ans+=['1']
            ans+=(small[:])
            m+=(ans[:])
            ans=m
            
        return ans[k-1]