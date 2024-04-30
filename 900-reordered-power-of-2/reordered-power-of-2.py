class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(0,32):
            if Solution.check(1<<i,n):
                return True
        return False
    def check(val,n):
        val=str(val)
        n=str(n)
        if(len(n)!=len(val)):return False
        for i in n:
            if n.count(i)!=val.count(i):
                return False
        return True