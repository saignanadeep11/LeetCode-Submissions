class Solution:
    def rotateString(self, s: str, g: str) -> bool:
        if s==g:
            return True
        n=len(s)
        if n!=len(g):
            return False
        ans=s
        for i in range(n):
            ans=ans[1:]+ans[0]
            if ans==g:
                return True
        return False