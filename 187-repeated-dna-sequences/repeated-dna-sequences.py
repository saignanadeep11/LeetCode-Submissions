class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=set()
        n=len(s)
        for i in range(n):
            # print(s[i:i+10] , s[i+10:],n)
            # print(s[i:i+10] in s[i+10:])
            if s[i:i+10] in s[i+1:]:
                ans.add(s[i:i+10])
        return ans