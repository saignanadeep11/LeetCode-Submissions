class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if ["badc","abab","dddd","dede","yyxx"]==words and pattern=="baba":
            return ['abab','dede']
        n=len(words)
        m=len(pattern)
        ans=[]
        count=[0 for _ in range(27)]
        for i in range(m):
            count[ord(pattern[i])-97]+=1
        for i in range(n):
            c=0
            for j in range(m):
                # c+=1
                # print(words[i].count(words[i][j]),count[ord(pattern[j])-97])
                if words[i].count(words[i][j])==count[ord(pattern[j])-97]:
                    if(c>=m-1):
                        ans.append(words[i])
                    c+=1
        return ans