class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:        
        c=0
        for i in derived:
            if i==1:
                c+=1
        if c%2==0:
            return True
        return False