class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            flag=0
            for j in i:
                if j not in allowed:
                    flag=1
                    break
            if flag==0:
                c+=1
        return c