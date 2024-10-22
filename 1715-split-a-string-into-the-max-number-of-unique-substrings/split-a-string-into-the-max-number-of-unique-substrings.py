class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        n=len(s)
        # res=0
        def find(arr,idx):
            if(idx>=n):
                return 0
            res=0
            for i in range(idx+1,n+1):
                ans=s[idx:i]
                if ans not in arr:
                    arr.append(ans)
                    res=max(res,1+find(arr,i))
                    arr.pop()
            # print(arr,res)
            # self.res=max(self.res,len(set(arr)))
            return res
        return find([],0)
        