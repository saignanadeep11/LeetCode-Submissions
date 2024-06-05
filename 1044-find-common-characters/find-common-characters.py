class Solution:
    def commonChars(self, words: List[str]) -> List[str]: 
        res=[]
        for i in range(0,27):
            m=2000000
            for j in words:
                c=j.count(chr(i+96))
                m=min(m,c)
                if m==0:
                    break
            if m>0:
                res+=(chr(i+96)*m)
        return res