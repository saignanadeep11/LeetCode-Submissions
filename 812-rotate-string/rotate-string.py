class Solution:
    def rotateString(self, s: str, g: str) -> bool:
        if s==g:
            return True
        if len(s)!=len(g):
            return False
        if s in g+g:
                return True
        return False