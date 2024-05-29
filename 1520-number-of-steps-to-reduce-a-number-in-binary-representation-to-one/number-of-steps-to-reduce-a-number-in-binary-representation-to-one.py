class Solution:
    def numSteps(self, s: str) -> int:
        
        n=int(s,2)
        step=0
        # print(n)
        while(n>1):
            if n%2!=0:
                n+=1
            else:
                n=n//2
            step+=1
            # print(n,step)
        return step