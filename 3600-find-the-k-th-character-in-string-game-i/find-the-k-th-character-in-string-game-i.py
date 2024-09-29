class Solution:
    def kthCharacter(self, k: int) -> str:
        ans="a"
        while(len(ans)<k):
            sAns=""
            for i in ans:
                if i=='z':
                    sAns+='a'
                else:
                    sAns+=chr(ord(i)+1)
            ans+=sAns
        # print(ans,len(ans))
        return ans[k-1]