class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr=[i*i for i in range(int(sqrt(c))+1)]
        p1=0
        p2=len(arr)-1
        if c==1 or c==2 or c==0:
            return True
        while(p1<=p2):
            k=arr[p1]+arr[p2]
            if k==c:
                return True
            elif k>c:
                p2-=1
            else:
                p1+=1
        return False