class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=dict()
        
        s1=list(s1.split(' '))
        s2=list(s2.split(' '))
        
        for i in s1:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        for i in s2:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        ans=[]
        for i in s:
            if(s[i]==1):
                ans.append(i)
        return ans
    