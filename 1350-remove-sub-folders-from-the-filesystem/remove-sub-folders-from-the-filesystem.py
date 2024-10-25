class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda k:len(k))
        ret=set()
        def check(s):
            for i in s:
                if i=='/':
                    return False
            return True
        for s in folder:
            n=len(s)
            small=""
            for i in range(n):
                if i!=0 and s[i]=='/':
                    # print(small,ret)
                    if small not in ret and check(s[i+1:]):
                        ret.add(s)
                        break
                    elif(small in ret):
                        break
                small+=s[i]
            if(small==s):
                ret.add(s)
        return list(ret)