class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        arr=sentence.split(" ")
        ans=""
        for i in arr:
            s=""
            flag=True
            for j in i:
                if s in dictionary:
                    ans+=s+" "
                    flag=False
                    break
                s+=j
            if flag:
                ans+=s+" "
        return ans[:-1]
        