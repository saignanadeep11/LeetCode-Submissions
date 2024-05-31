class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        e=0
        a=0
        b=0
        for i in nums:
            e=e^i
        def check(x,i):
            return (x &(1<<i))!=0
        pos=0
        for i  in range(31):
            if(check(e,i)):
                pos=i
        for i in nums:
            if(check(i,pos)):
                a^=i
            else:
                b^=i

        return [a,b]