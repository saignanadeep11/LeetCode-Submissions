class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:return n
        total=(n*(n+1))/2

        for i in range(1,n):
            f1=(i*(i+1))//2
            if (total-f1+i==f1):
                return i
        return -1