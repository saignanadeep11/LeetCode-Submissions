class Solution:
    def countStudents(self, stu: List[int], san: List[int]) -> int:
        n=len(san)
        one=stu.count(1)
        zero=stu.count(0)
        c=0
        for i in san:
            if i==0:
                if zero>0:
                    c+=1
                    zero-=1
                else:
                    return n-c
            else:
                if one>0: 
                    c+=1
                    one-=1
                else: return n-c
            
        return n-c