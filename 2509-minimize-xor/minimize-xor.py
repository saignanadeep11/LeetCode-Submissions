class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def setBits(n):
            c=0
            for i in range(32):
                if (n>>i)&1==1:
                    c+=1
            return c
        count=setBits(num2)
        # print(count)
        ans=0
        for i in range(33,-1,-1):
            if count==0:
                return ans
            if (1<<i)&num1:
                ans=ans|(1<<i)
                count-=1
            # print(ans,i,1<<i,(1<<i)&num1)
        idx=0
        # print(ans,count)
        while(count>0):
            if not (1<<idx)&num1:
                ans=ans|(1<<idx)
                count-=1
            idx+=1
            # print(idx,ans,count)
        return ans