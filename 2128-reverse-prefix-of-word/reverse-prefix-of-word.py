class Solution:
    def reversePrefix(self, s: str, ch: str) -> str:
        i=s.find(ch,0)
        
        a=(s[:i+1])
        a=a[::-1]+s[i+1:]
        
        return a