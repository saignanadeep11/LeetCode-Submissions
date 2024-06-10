class Solution:
    def plusOne(self, dig: List[int]) -> List[int]:
        ans=[]
        n=len(dig)
        c=s=0
        for i in range(n-1,-1,-1):
            if i==n-1:
                c=dig[i]+1
            # print(c,s)
            s=c//10
            c=c%10
            ans.insert(0,c)
            if i>=1:
                c=dig[i-1]+s
            # print(c,s)
        if s:
            ans.insert(0,s+c)
        return ans