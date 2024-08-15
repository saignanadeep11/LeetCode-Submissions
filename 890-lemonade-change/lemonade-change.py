class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=0
        t=0
        for i in bills:
            if i==5:
                f+=1
                continue
            if i==10:
                if f<1:
                    return False
                f-=1
                t+=1
                continue
            if t>0 and f>0:
                t-=1
                f-=1
            elif f>2:
                f-=3
            else:
                return False
            
        return True