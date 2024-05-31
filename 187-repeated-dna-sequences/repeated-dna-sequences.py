class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=set()
        rep=set()
        n=len(s)
        for i in range(n-9):
            
            k=s[i:i+10]
            if k in ans:
                rep.add(k)
            else:
                ans.add(k)
        return rep